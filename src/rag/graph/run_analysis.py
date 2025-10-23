import os
import json
import logging

import networkx as nx

from src.settings import CONTENT_DIR, INDEX_DIR
from .graph_builder import create_graph_rag_index
from .graph_analysis import GraphAnalyzer

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_and_analyze_graph(
    content_dir: str = CONTENT_DIR, 
    index_dir: str = INDEX_DIR, 
    visualize: bool = True
):
    """
    Create graph index and perform comprehensive analysis
    
    :param content_dir: Directory containing content
    :param index_dir: Directory to store index
    :param visualize: Whether to generate graph visualization
    :return: Graph builder instance
    """
    # Create graph index
    graph_builder = create_graph_rag_index(content_dir, index_dir)
    graph = graph_builder.graph
    
    # Create graph analyzer
    graph_analyzer = GraphAnalyzer(graph)
    
    # Perform analyses
    logger.info("Performing Graph Analyses")
    
    # 1. Node Type Counts
    logger.info("\n1. Node Type Counts:")
    type_counts = graph_analyzer.count_nodes_by_type()
    for node_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
        logger.info(f"- {node_type}: {count}")
    
    # 2. Most Connected Nodes
    logger.info("\n2. Most Connected Nodes:")
    most_connected = graph_analyzer.find_most_connected_nodes(top_k=10)
    for node in most_connected:
        logger.info(
            f"- {node['node']} "
            f"(Type: {node['type']}, "
            f"Connections: {node['total_connections']})"
        )
    
    # 3. Visualize Graph
    if visualize:
        visualization_path = os.path.join(index_dir, 'campaign_graph.png')
        graph_analyzer.visualize_graph(visualization_path)
    
    return graph_builder

def interactive_graph_explorer(graph_builder):
    """
    Interactive graph exploration function
    
    :param graph_builder: Graph builder instance
    """
    graph_analyzer = GraphAnalyzer(graph_builder.graph)
    
    while True:
        print("\n--- Graph Explorer ---")
        print("1. Explore an Entity")
        print("2. Graph Overview")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            entity = input("Enter entity name to explore: ").strip()
            try:
                # Use explore_node method from GraphAnalyzer
                exploration = graph_analyzer.explore_node(entity)
                print(json.dumps(exploration, indent=2))
            except Exception as e:
                print(f"Error exploring entity: {e}")
        
        elif choice == '2':
            # Reuse the analysis from run_and_analyze_graph
            type_counts = graph_analyzer.count_nodes_by_type()
            print("\n1. Node Type Counts:")
            for node_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
                print(f"- {node_type}: {count}")
            
            print("\n2. Most Connected Nodes:")
            most_connected = graph_analyzer.find_most_connected_nodes(top_k=10)
            for node in most_connected:
                print(
                    f"- {node['node']} "
                    f"(Type: {node['type']}, "
                    f"Connections: {node['total_connections']})"
                )
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == '__main__':
    # Run graph analysis
    graph_builder = run_and_analyze_graph()
    
    # Optional: Start interactive explorer
    interactive_choice = input("Start interactive graph explorer? (y/n): ").strip().lower()
    if interactive_choice == 'y':
        interactive_graph_explorer(graph_builder)
