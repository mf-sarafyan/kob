import os
import logging
from typing import Dict, List, Any, Optional

import networkx as nx

from .graph_builder import ObsidianGraphBuilder
from .graph_navigation import GraphNavigator
from .graph_analysis import GraphAnalyzer
from .text_processing import normalize_entity_name

logger = logging.getLogger(__name__)

class KnowledgeGraph:
    """
    Comprehensive knowledge graph with building, navigation, and analysis capabilities
    """
    def __init__(self, content_dir: str, index_dir: str):
        """
        Initialize the knowledge graph
        
        :param content_dir: Directory containing content files
        :param index_dir: Directory for storing graph index
        """
        # Graph builder for creating the graph
        self.builder = ObsidianGraphBuilder(content_dir)
        
        # Build or load the graph
        self.graph = self._build_or_load_graph(content_dir, index_dir)
        
        # Navigation utilities
        self.navigator = GraphNavigator(self.graph)
        
        # Analysis utilities
        self.analyzer = GraphAnalyzer(self.graph)
    
    def _build_or_load_graph(self, content_dir: str, index_dir: str) -> nx.MultiDiGraph:
        """
        Build or load the graph from index
        
        :param content_dir: Directory containing content files
        :param index_dir: Directory for storing graph index
        :return: NetworkX MultiDiGraph
        """
        # Ensure index directory exists
        os.makedirs(index_dir, exist_ok=True)
        
        # Check if an existing index exists
        index_file = os.path.join(index_dir, 'campaign_graph.json')
        
        # Try to load existing graph
        if os.path.exists(index_file):
            try:
                logger.info("Loading existing graph index")
                graph = ObsidianGraphBuilder.load_graph(index_file)
                logger.info(f"Loaded graph with {len(graph.nodes)} nodes and {len(graph.edges)} edges")
                return graph
            except Exception as e:
                logger.warning(f"Could not load existing graph: {e}. Building new graph.")
        
        # Build the graph
        logger.info("Building graph from content")
        graph = self.builder.build_graph()
        
        # Export the graph using builder's export method
        try:
            self.builder.export_graph(index_file)
            logger.info(f"Exported graph index to {index_file}")
        except Exception as e:
            logger.error(f"Could not export graph index: {e}")
        
        return graph
    
    def find_entity(self, search_term: str) -> List[Dict[str, Any]]:
        """
        Find entities matching the search term
        
        :param search_term: Search term to find entities
        :return: List of matching entities
        """
        return self.navigator.find_node_by_name_or_alias(search_term)
    
    def get_entity_details(self, entity_name: str) -> Dict[str, Any]:
        """
        Get comprehensive details for an entity
        
        :param entity_name: Name of the entity
        :return: Entity details
        """
        return self.navigator.get_node_content(entity_name)
    
    def get_related_entities(self, entity_name: str, max_depth: int = 2) -> Dict[str, Any]:
        """
        Get related entities for a given entity
        
        :param entity_name: Name of the starting entity
        :param max_depth: Maximum depth of exploration
        :return: Related entities
        """
        return self.navigator.get_related_nodes(entity_name, max_depth)
    
    def analyze_graph_connectivity(self) -> Dict[str, Any]:
        """
        Analyze overall graph connectivity
        
        :return: Graph connectivity report
        """
        return self.analyzer.diagnose_graph_connectivity()
    
    def visualize_graph(self, output_path: Optional[str] = None):
        """
        Visualize the graph
        
        :param output_path: Path to save the graph visualization
        """
        self.analyzer.visualize_graph(output_path)

def create_knowledge_graph(
    content_dir: str = None, 
    index_dir: str = None
) -> KnowledgeGraph:
    """
    Create a knowledge graph
    
    :param content_dir: Directory containing content files
    :param index_dir: Directory for storing graph index
    :return: Configured KnowledgeGraph instance
    """
    from src.settings import CONTENT_DIR, INDEX_DIR
    
    content_dir = content_dir or CONTENT_DIR
    index_dir = index_dir or INDEX_DIR
    
    return KnowledgeGraph(content_dir, index_dir)
