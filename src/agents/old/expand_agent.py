import os
import logging
from typing import Dict, List, Any, Optional

import networkx as nx
from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import ChatOllama

from src.settings import CONTENT_DIR, INDEX_DIR
from src.rag import create_knowledge_graph

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Pydantic model for document selection
class DocumentSelector(BaseModel):
    """
    Structured model for document selection
    """
    relevant_documents: List[str] = Field(
        default_factory=list, 
        description="List of document names that are MOST relevant"
    )
    reasoning: Optional[str] = Field(
        default=None, 
        description="Explanation of why these documents were selected"
    )
    error: Optional[str] = None

# Prompt template for document selection
document_selector_prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an expert document selector for a comprehensive D&D campaign knowledge base. "
     "Your task is to intelligently select the most relevant documents to provide context for the given query. "
     "\n\nGuidelines for Document Selection:\n"
     "1. Comprehensive Context Gathering:\n"
     "   - Include documents that directly answer the query\n"
     "   - Include related documents that provide additional context\n"
     "   - Consider character backgrounds, relationships, locations, and events\n"
     "   - Look for interconnected information across different document types\n"
     "\n2. Breadth and Depth:\n"
     "   - Don't limit yourself to just the most obvious documents\n"
     "   - Explore tangential but potentially illuminating sources\n"
     "   - Balance between direct relevance and contextual richness\n"
     "\n3. Selection Strategy:\n"
     "   - Aim for 5-15 documents depending on query complexity\n"
     "   - Prefer quality and comprehensiveness over strict limitation\n"
     "   - Include documents from different categories if they add value\n"
     "\n4. Reasoning:\n"
     "   - Provide a clear, concise explanation of your selection\n"
     "   - Highlight the connections between selected documents\n"
     "\n5. JSON Output Requirements:\n"
     "```json\n"
     "{{\n"
     '  "relevant_documents": ["Document1", "Document2", ...],\n'
     '  "reasoning": "Detailed explanation of document selection strategy",\n'
     '  "error": null\n'
     "}}\n"
     "```\n"
     "\nImportant: Always return a valid JSON, even if the document list is empty."
    ),
    ("user", 
     "Query: {query}\n\n"
     "Available Documents:\n{available_documents}\n\n"
     "Context: Provide a comprehensive set of documents that will help answer the query "
     "by offering multiple perspectives and detailed information."
    ),
    ("assistant", "{output_format}")
])

# LLM for document selection
document_selector_llm = ChatOllama(
    model="qwen2.5:7b-instruct",  # or "llama3.1:8b-instruct"
    temperature=0.1,
    num_ctx=1024,
)

# JSON output parser for document selection
document_selector_parser = JsonOutputParser(pydantic_object=DocumentSelector)

# Combine prompt, LLM, and parser
document_selector_chain = document_selector_prompt | document_selector_llm | document_selector_parser

class ExpandAgent:
    def __init__(
        self, 
        content_dir: str = CONTENT_DIR,
        index_dir: str = INDEX_DIR
    ):
        """
        Initialize the expand agent
        
        :param content_dir: Directory containing content
        :param index_dir: Directory for storing indexes
        """
        # Create Knowledge Graph
        self.knowledge_graph = create_knowledge_graph(
            content_dir=content_dir, 
            index_dir=index_dir
        )
    
    def find_adjacent_entities(self, entities: List[str]) -> List[Dict[str, Any]]:
        """
        Find adjacent entities and their connections
        
        :param entities: List of initial entities to expand from
        :return: List of dictionaries with entity details and connections
        """
        enriched_entities = []
        
        for entity in entities:
            try:
                # Get related entities
                related_entities = self.knowledge_graph.get_related_entities(entity)
                
                # Prepare enriched entity information
                enriched_entity = {
                    'entity_name': entity,
                    'type': self.knowledge_graph.get_entity_details(entity).get('node_type', 'unknown'),
                    'connections': [
                        {'node_name': node, **details} 
                        for node, details in related_entities.get('direct_connections', {}).items()
                    ]
                }
                
                enriched_entities.append(enriched_entity)
            
            except Exception as e:
                # Log any errors but continue processing
                logger.warning(f"Error finding connections for {entity}: {e}")
                enriched_entities.append({
                    'entity_name': entity,
                    'type': 'unknown',
                    'connections': [],
                    'error': str(e)
                })
        
        return enriched_entities
    
    def select_documents(self, query: str, available_documents: List[str]) -> Dict[str, Any]:
        """
        Select the most relevant documents
        
        :param query: Original user query
        :param available_documents: List of available documents
        :return: Structured selection of relevant documents
        """
        try:
            # Invoke document selector
            selection = document_selector_chain.invoke({
                'query': query,
                'available_documents': "\n".join(available_documents),
                'output_format': (
                    "Provide a JSON with:\n"
                    "- relevant_documents: List of all relevant document names, which may be multiple\n"
                    "- reasoning: Why these were selected\n"
                    "- error: If any, an error message\n"
                )
            })
            
            return selection
        
        except Exception as e:
            logger.error(f"Document selection error: {e}")
            return {
                'relevant_documents': [],
                'reasoning': f"Error in document selection: {str(e)}",
                'error': str(e)
            }
    
    def retrieve_document_contents(self, selected_documents: List[str]) -> Dict[str, str]:
        """
        Retrieve full contents for selected documents from the graph
        
        :param selected_documents: List of document names to retrieve
        :return: Dictionary of document contents
        """
        try:
            # Use knowledge graph to retrieve document contents
            return {
                doc: self.knowledge_graph.get_entity_details(doc).get('content', {}).get('full_content', 'No content available')
                for doc in selected_documents
            }
        except Exception as e:
            logger.error(f"Error retrieving document contents: {e}")
            return {
                doc: f"Error retrieving content: {str(e)}" 
                for doc in selected_documents
            }
    
    def __call__(self, query: str, search_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full document expansion process
        
        :param query: User query
        :param search_result: Initial search results
        :return: Expanded context with selected documents and contents
        """
        # Collect all entities from search results
        entities = []
        
        # Collect from vector search results
        for vector_search in search_result.get('vector_searches', []):
            if isinstance(vector_search.get('results', []), list):
                entities.extend([
                    doc.get('name', '') for doc in vector_search.get('results', [])
                ])
        
        # Collect from graph search results
        for graph_search in search_result.get('graph_searches', []):
            if isinstance(graph_search.get('results', []), list):
                entities.extend([
                    doc.get('node', '') for doc in graph_search.get('results', [])
                ])
            elif isinstance(graph_search.get('results', {}), dict):
                entities.append(
                    graph_search.get('results', {}).get('node', '')
                )
        
        # Remove duplicates and empty entities
        entities = list(set(filter(bool, entities)))
        
        # Find adjacent entities
        adjacent_entities = self.find_adjacent_entities(entities)
        
        # Collect all available documents
        available_documents = entities.copy()
        for entity in adjacent_entities:
            available_documents.extend([
                conn['node_name'] for conn in entity.get('connections', [])
            ])
        
        # Remove duplicates and empty strings
        available_documents = list(set(filter(bool, available_documents)))
        
        # Select relevant documents
        document_selection = self.select_documents(query, available_documents)
        
        # Retrieve document contents
        document_contents = self.retrieve_document_contents(
            document_selection.get('relevant_documents', [])
        )
        
        # Combine results
        return {
            'query': query,
            'initial_entities': entities,
            'adjacent_entities': adjacent_entities,
            'document_selection': document_selection,
            'document_contents': document_contents
        }

def create_expand_agent(
    content_dir: str = CONTENT_DIR, 
    index_dir: str = INDEX_DIR
) -> ExpandAgent:
    """
    Create an expand agent
    
    :param content_dir: Directory containing content
    :param index_dir: Directory for storing indexes
    :return: Configured ExpandAgent
    """
    return ExpandAgent(
        content_dir=content_dir, 
        index_dir=index_dir
    )

# Main execution for testing
if __name__ == '__main__':
    from src.agents.old.search_agent import create_search_agent
    
    # Create search and expand agents
    search_agent = create_search_agent()
    expand_agent = create_expand_agent()
    
    # Test queries
    test_queries = [
        "What's the Rock of Bral political structure",
        "Who is Baang",
        "Who are the Keepers?",
        "Who is Vax",
        "What are the current events in the campaign",
        "How do I set up a Bastion?", 
        "What is The Spelljammer"
    ]
    
    # Run searches and expansions
    import json
    for query in test_queries:
        print(f"\n=== Query: {query} ===")
        
        # Perform search
        search_result = search_agent(query)
        
        # Expand context
        expand_result = expand_agent(query, search_result)
        
        print(json.dumps(expand_result, indent=2))
