import os
import logging
from typing import Dict, Any, Optional, List, Tuple

from langchain.tools import BaseTool
from pydantic import BaseModel, Field, ConfigDict
from langchain_community.vectorstores import FAISS

from src.rag.search import VectorSearchAugmenter
from src.rag.index import create_rag_index
from src.rag.graph.main_graph import create_knowledge_graph
from src.settings import CONTENT_DIR, INDEX_DIR
from src.rag.graph.graph_builder import ObsidianGraphBuilder
from src.rag.graph.graph_analysis import GraphAnalyzer

logger = logging.getLogger(__name__)

class KnowledgeGraphToolInput(BaseModel):
    """Input model for knowledge graph tools."""
    query: str = Field(description="Search query or entity name")
    max_depth: int = Field(default=2, description="Maximum depth for related entities search")

class SearchEntityTool(BaseTool):
    """Tool to search for entities in the knowledge graph."""
    name: str = "search_entity"
    description: str = "Search for entities in the knowledge graph by name or alias"
    
    # Declare kg as a field to avoid Pydantic validation errors
    kg: Any = Field(default=None, exclude=True)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.kg is None:
            # Lazy initialization - create kg when first needed
            object.__setattr__(self, 'kg', create_knowledge_graph())
    
    def _run(self, query: str) -> str:
        """Run the search entity tool."""
        try:
            # Ensure kg is initialized
            if self.kg is None:
                object.__setattr__(self, 'kg', create_knowledge_graph())
            
            results = self.kg.find_entity(query)
            if not results:
                return "No entities found matching the search term."
            
            # Format results as a readable string
            formatted_results = "\n".join([
                f"- {entity['node']} (Type: {entity['type']})" 
                for entity in results
            ])
            return f"Matching Entities:\n{formatted_results}"
        except Exception as e:
            return f"Error searching entities: {str(e)}"
    
    def _arun(self, query: str):
        """Async run method (not implemented)."""
        raise NotImplementedError("SearchEntityTool does not support async operations")

class EntityDetailsTool(BaseTool):
    """Tool to retrieve content and attributes for an entity."""
    name: str = "entity_details"
    description: str = (
        "Get the full content and attributes for a specific entity in the knowledge graph. "
        "Returns all content without truncation. Use entity_connections to see relationships to other entities."
    )
    
    # Declare kg as a field to avoid Pydantic validation errors
    kg: Any = Field(default=None, exclude=True)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.kg is None:
            # Lazy initialization - create kg when first needed
            object.__setattr__(self, 'kg', create_knowledge_graph())
    
    def _run(self, query: str) -> str:
        """Run the entity details tool - returns content only."""
        try:
            # Ensure kg is initialized
            if self.kg is None:
                object.__setattr__(self, 'kg', create_knowledge_graph())
            
            details = self.kg.get_entity_details(query)
            
            # Check for error
            if isinstance(details, dict) and 'error' in details:
                return f"Error: {details['error']}"
            
            # Format the output nicely - CONTENT ONLY, NO TRUNCATION
            formatted_lines = []
            formatted_lines.append(f"=== Entity Details for '{query}' ===\n")
            
            # Entity type
            entity_type = details.get('node_type', 'unknown')
            formatted_lines.append(f"Type: {entity_type}")
            
            # Node attributes (if any)
            node_attrs = details.get('node_attributes', {})
            if node_attrs:
                formatted_lines.append(f"\nAttributes:")
                for key, value in node_attrs.items():
                    if value:  # Only show non-empty values
                        formatted_lines.append(f"  - {key}: {value}")
            
            # Content - FULL CONTENT, NO TRUNCATION
            content = details.get('content', {})
            full_content = content.get('full_content', '')
            if full_content:
                formatted_lines.append(f"\nContent:")
                formatted_lines.append(full_content)
            else:
                formatted_lines.append(f"\nContent: No content available")
            
            # Note about connections
            formatted_lines.append(f"\n💡 To see connections to other entities, use entity_connections tool.")
            
            return "\n".join(formatted_lines)
        except Exception as e:
            logger.error(f"Error in entity_details tool: {e}")
            return f"Error retrieving entity details: {str(e)}"
    
    def _arun(self, query: str):
        """Async run method (not implemented)."""
        raise NotImplementedError("EntityDetailsTool does not support async operations")

class EntityConnectionsTool(BaseTool):
    """Tool to retrieve connections/relationships for an entity."""
    name: str = "entity_connections"
    description: str = (
        "Get all connections (relationships) for a specific entity in the knowledge graph. "
        "Shows which entities are connected to this entity and how. "
        "Use the connected entity names with entity_details to explore them further."
    )
    
    # Declare kg as a field to avoid Pydantic validation errors
    kg: Any = Field(default=None, exclude=True)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.kg is None:
            # Lazy initialization - create kg when first needed
            object.__setattr__(self, 'kg', create_knowledge_graph())
    
    def _run(self, query: str) -> str:
        """Run the entity connections tool - returns connections only."""
        try:
            # Ensure kg is initialized
            if self.kg is None:
                object.__setattr__(self, 'kg', create_knowledge_graph())
            
            details = self.kg.get_entity_details(query)
            
            # Check for error
            if isinstance(details, dict) and 'error' in details:
                return f"Error: {details['error']}"
            
            # Format connections
            formatted_lines = []
            formatted_lines.append(f"=== Connections for '{query}' ===\n")
            
            connections = details.get('connections', {})
            incoming = connections.get('incoming', [])
            outgoing = connections.get('outgoing', [])
            
            if incoming or outgoing:
                if outgoing:
                    formatted_lines.append(f"Connected To ({len(outgoing)} entities):")
                    # Group by relationship type for clarity
                    by_relation = {}
                    for conn in outgoing:
                        rel_type = conn.get('edge_type', 'unknown')
                        if rel_type not in by_relation:
                            by_relation[rel_type] = []
                        by_relation[rel_type].append(conn)
                    
                    for rel_type, conns in by_relation.items():
                        formatted_lines.append(f"\n  {rel_type}:")
                        for conn in conns:
                            target = conn.get('target_node', 'unknown')
                            target_type = conn.get('target_type', 'unknown')
                            formatted_lines.append(f"    → {target} (Type: {target_type})")
                
                if incoming:
                    formatted_lines.append(f"\n\nConnected From ({len(incoming)} entities):")
                    # Group by relationship type
                    by_relation = {}
                    for conn in incoming:
                        rel_type = conn.get('edge_type', 'unknown')
                        if rel_type not in by_relation:
                            by_relation[rel_type] = []
                        by_relation[rel_type].append(conn)
                    
                    for rel_type, conns in by_relation.items():
                        formatted_lines.append(f"\n  {rel_type}:")
                        for conn in conns:
                            source = conn.get('source_node', 'unknown')
                            source_type = conn.get('source_type', 'unknown')
                            formatted_lines.append(f"    ← {source} (Type: {source_type})")
                
                formatted_lines.append(f"\n\n💡 Tip: You can explore these connected entities using:")
                formatted_lines.append(f"   - entity_details: Get full content for a specific connected entity")
                formatted_lines.append(f"   - entity_connections: Get connections for a connected entity")
                formatted_lines.append(f"   - related_entities: Get all related entities with deep exploration")
                formatted_lines.append(f"   - graph_search: Explore graph connections more deeply")
            else:
                formatted_lines.append("No connections found")
            
            return "\n".join(formatted_lines)
        except Exception as e:
            logger.error(f"Error in entity_connections tool: {e}")
            return f"Error retrieving entity connections: {str(e)}"
    
    def _arun(self, query: str):
        """Async run method (not implemented)."""
        raise NotImplementedError("EntityConnectionsTool does not support async operations")

class RelatedEntitiesTool(BaseTool):
    """Tool to find related entities in the knowledge graph."""
    name: str = "related_entities"
    description: str = "Find related entities for a given entity with a specified maximum depth"
    
    # Declare kg as a field to avoid Pydantic validation errors
    kg: Any = Field(default=None, exclude=True)
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.kg is None:
            # Lazy initialization - create kg when first needed
            object.__setattr__(self, 'kg', create_knowledge_graph())
    
    def _run(self, query: str, max_depth: int = 2) -> str:
        """Run the related entities tool."""
        try:
            # Ensure kg is initialized
            if self.kg is None:
                object.__setattr__(self, 'kg', create_knowledge_graph())
            
            related = self.kg.get_related_entities(query, max_depth)
            return f"Related Entities for '{query}':\n{related}"
        except Exception as e:
            return f"Error retrieving related entities: {str(e)}"
    
    def _arun(self, query: str):
        """Async run method (not implemented)."""
        raise NotImplementedError("RelatedEntitiesTool does not support async operations")

class VectorSearchTool(BaseTool):
    """
    LangChain Tool for Vector Search
    Wraps VectorSearchAugmenter from src.rag.search
    Returns formatted string with entity names that can be explored further.
    """
    name: str = "vector_search"
    description: str = (
        "Performs a semantic search across documents, "
        "returning relevant entities and their context. "
        "Use this when search_entity doesn't find results or when searching semantically. "
        "The returned entities can be explored further using entity_details or related_entities tools."
    )
    
    vector_search_augmenter: VectorSearchAugmenter
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    def _run(
        self, 
        query: str, 
        return_type: str = 'entities'
    ) -> str:
        """
        Run vector search and format results as a string
        
        :param query: Search query
        :param return_type: 'entities' or 'documents' (entities is recommended)
        :return: Formatted string with entity information
        """
        try:
            results = self.vector_search_augmenter.search(query, return_type)
            
            if not results:
                return f"No entities found for query: '{query}'. Try rephrasing your search or using search_entity with specific names."
            
            # Format results as a readable string similar to search_entity
            if return_type == 'entities':
                formatted_lines = ["Vector Search Results:"]
                formatted_lines.append(f"Found {len(results)} relevant entities:\n")
                
                for entity in results:
                    entity_name = entity.get('name', 'Unknown')
                    entity_type = entity.get('type', 'unknown')
                    doc_count = len(entity.get('related_documents', []))
                    
                    formatted_lines.append(f"- {entity_name} (Type: {entity_type})")
                    formatted_lines.append(f"  Found in {doc_count} document chunk(s)")
                    
                    # Add a brief summary if available
                    details = entity.get('details', {})
                    if details:
                        # Try to get a brief description or key info
                        summary_parts = []
                        for key in ['description', 'summary', 'title']:
                            if key in details and details[key]:
                                summary_parts.append(str(details[key])[:100])
                                break
                        if summary_parts:
                            formatted_lines.append(f"  Info: {summary_parts[0]}")
                
                formatted_lines.append("\nYou can explore these entities further using:")
                formatted_lines.append("- entity_details tool to get comprehensive information")
                formatted_lines.append("- related_entities tool to find connected entities")
                formatted_lines.append("- graph_search tool to explore graph connections")
                
                return "\n".join(formatted_lines)
            else:
                # For documents return type, format as documents
                formatted_lines = [f"Found {len(results)} relevant documents:\n"]
                for i, doc in enumerate(results, 1):
                    source = doc.metadata.get('source', 'unknown')
                    parent_entity = doc.metadata.get('parent_entity', 'unknown')
                    formatted_lines.append(f"{i}. Source: {source}")
                    formatted_lines.append(f"   Entity: {parent_entity}")
                    formatted_lines.append(f"   Content: {doc.page_content[:200]}...\n")
                return "\n".join(formatted_lines)
                
        except Exception as e:
            logger.error(f"Vector search error: {e}")
            return f"Error performing vector search: {str(e)}"
    
    async def _arun(
        self, 
        query: str, 
        return_type: str = 'entities'
    ) -> str:
        """
        Async run vector search
        """
        return self._run(query, return_type)

class GraphSearchTool(BaseTool):
    """
    LangChain Tool for Graph-based Entity Search
    Wraps GraphAnalyzer from src.rag.graph.graph_analysis
    """
    name: str = "graph_search"
    description: str = (
        "Searches for entities in the graph, "
        "returning their connections and details."
    )
    
    graph_builder: ObsidianGraphBuilder
    graph_analyzer: GraphAnalyzer
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    def _run(
        self, 
        entity_name: str, 
        max_depth: int = 2,
        relationship_types: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Run graph search
        
        :param entity_name: Name of the entity to search
        :param max_depth: Maximum depth of graph exploration
        :param relationship_types: Optional list of relationship types to filter
        :return: Graph search results
        """
        try:
            # Explore the node using graph analyzer
            node_details = self.graph_analyzer.explore_node(
                entity_name, 
                max_depth=max_depth
            )
            
            # Filter relationships if specified
            if relationship_types:
                filtered_relationships = {}
                for rel_type, connections in node_details.get('relationships', {}).items():
                    if rel_type in relationship_types:
                        filtered_relationships[rel_type] = connections
                node_details['relationships'] = filtered_relationships
            
            return node_details
        
        except Exception as e:
            logger.error(f"Graph search error for {entity_name}: {e}")
            return {
                'error': str(e),
                'entity': entity_name
            }
    
    async def _arun(
        self, 
        entity_name: str, 
        max_depth: int = 2,
        relationship_types: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Async run graph search
        """
        return self._run(entity_name, max_depth, relationship_types)

def create_search_tools(
    vector_store: FAISS, 
    graph_builder: ObsidianGraphBuilder,
    top_k: int = 5
) -> Tuple[VectorSearchTool, GraphSearchTool]:
    """
    Create vector and graph search tools
    
    :param vector_store: FAISS vector store
    :param graph_builder: Obsidian graph builder
    :param top_k: Number of top results to retrieve
    :return: Tuple of (VectorSearchTool, GraphSearchTool)
    """
    # Create Vector Search Augmenter (core logic, no LangChain)
    vector_search_augmenter = VectorSearchAugmenter(
        vector_store, 
        graph_builder, 
        top_k=top_k
    )
    
    # Create Graph Analyzer (core logic, no LangChain)
    graph_analyzer = GraphAnalyzer(graph_builder.graph)
    
    # Create LangChain tool wrappers
    vector_search_tool = VectorSearchTool(
        vector_search_augmenter=vector_search_augmenter
    )
    
    graph_search_tool = GraphSearchTool(
        graph_builder=graph_builder,
        graph_analyzer=graph_analyzer
    )
    
    return vector_search_tool, graph_search_tool

# Convenience function to get all graph tools
def get_graph_tools():
    """Return a list of all graph-related tools."""
    # Create RAG index to get vector_store and graph_builder
    vector_store, graph_builder, _ = create_rag_index(CONTENT_DIR, INDEX_DIR)
    
    # Create search tools using local create_search_tools function
    vector_search_tool, graph_search_tool = create_search_tools(
        vector_store, 
        graph_builder
    )
    
    return [
        SearchEntityTool(),
        EntityDetailsTool(),
        EntityConnectionsTool(),
        RelatedEntitiesTool(),
        vector_search_tool,
        graph_search_tool
    ]

