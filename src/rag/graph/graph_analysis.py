import os
import json
import logging
from typing import Dict, List, Any, Optional

import networkx as nx
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

class GraphAnalyzer:
    def __init__(self, graph: nx.MultiDiGraph):
        """
        Initialize graph analyzer with a given graph
        
        :param graph: NetworkX MultiDiGraph to analyze
        """
        self.graph = graph
    
    def count_nodes_by_type(self) -> Dict[str, int]:
        """
        Count nodes by their type
        
        :return: Dictionary of node type counts
        """
        type_counts = {}
        for _, node_data in self.graph.nodes(data=True):
            node_type = node_data.get('type', 'unknown')
            type_counts[node_type] = type_counts.get(node_type, 0) + 1
        
        return type_counts
    
    def find_most_connected_nodes(self, top_k: int = 10) -> List[Dict[str, Any]]:
        """
        Find nodes with the most connections (highest degree centrality)
        
        :param top_k: Number of top connected nodes to return
        :return: List of most connected nodes with their connection details
        """
        # Calculate node degrees
        node_degrees = {}
        for node in self.graph.nodes():
            # Count both in and out edges
            node_degrees[node] = self.graph.degree(node)
        
        # Sort nodes by degree (most connected first)
        most_connected = sorted(
            node_degrees.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:top_k]
        
        # Prepare detailed results
        results = []
        for node, degree in most_connected:
            node_data = dict(self.graph.nodes[node])
            results.append({
                'node': node,
                'type': node_data.get('type', 'unknown'),
                'total_connections': degree,
                'node_details': node_data
            })
        
        return results
    
    def explore_node(self, node_name: str, max_depth: int = 2) -> Dict[str, Any]:
        """
        Explore a node's connections in detail
        
        :param node_name: Name of the node to explore
        :param max_depth: Maximum depth of exploration
        :return: Detailed node exploration result
        """
        if node_name not in self.graph.nodes:
            return {"error": f"Node '{node_name}' not found in the graph"}
        
        # Get node details
        node_data = dict(self.graph.nodes[node_name])
        
        # Get the type of the starting node
        start_node_type = node_data.get('type', 'unknown')
        
        # Prepare exploration results
        exploration = {
            "node_name": node_name,
            "node_type": start_node_type,
            "node_attributes": node_data,
            "connections": {
                "direct": {},
                "indirect": {}
            }
        }
        
        # Direct connections (1-hop)
        for neighbor in self.graph.neighbors(node_name):
            edge_data = list(self.graph.get_edge_data(node_name, neighbor).values())[0]
            exploration["connections"]["direct"][neighbor] = {
                "type": self.graph.nodes[neighbor].get('type', 'unknown'),
                "edge_type": edge_data.get('type', 'unknown')
            }
        
        # Indirect connections (2-hop)
        if max_depth > 1:
            for neighbor in exploration["connections"]["direct"].keys():
                for indirect_neighbor in self.graph.neighbors(neighbor):
                    # Only add indirect connections of the same type as the starting node
                    if (indirect_neighbor != node_name and 
                        self.graph.nodes[indirect_neighbor].get('type') == start_node_type):
                        exploration["connections"]["indirect"][indirect_neighbor] = {
                            "type": self.graph.nodes[indirect_neighbor].get('type', 'unknown'),
                            "via": neighbor
                        }
        
        return exploration
    
    def visualize_graph(self, output_path: Optional[str] = None, max_nodes: int = 800):
        """
        Create a visualization of the graph with weighted edges
        
        :param output_path: Path to save the graph visualization
        :param max_nodes: Maximum number of nodes to visualize
        """
        # Limit graph size to prevent overwhelming visualization
        if len(self.graph.nodes) > max_nodes:
            print(f"Warning: Graph has {len(self.graph.nodes)} nodes. Sampling {max_nodes} nodes.")
            sampled_nodes = list(self.graph.nodes)[:max_nodes]
            subgraph = self.graph.subgraph(sampled_nodes)
        else:
            subgraph = self.graph
        
        # Prepare visualization
        plt.figure(figsize=(40, 40), dpi=300)  # Increased figure size and resolution
        pos = nx.spring_layout(subgraph, k=0.5, iterations=50, seed=42)
        
        # Enhanced color mapping for node types
        type_colors = {
            'character': '#3498db',  # Bright blue
            'faction': '#2ecc71',    # Bright green
            'location': '#e74c3c',   # Bright red
            'item': '#9b59b6',       # Purple
            'entry': '#f39c12',      # Orange
            'party': '#1abc9c',      # Turquoise
            'content_chunk': '#95a5a6',  # Gray for content chunks
            'unknown': '#34495e'     # Dark blue-gray
        }
        
        # Node colors with fallback
        node_colors = [
            type_colors.get(subgraph.nodes[node].get('type', 'unknown'), type_colors['unknown']) 
            for node in subgraph.nodes
        ]
        
        # Node sizes based on number of connections with min and max sizes
        node_sizes = [
            max(50, min(500, 100 + 20 * subgraph.degree(node))) 
            for node in subgraph.nodes
        ]
        
        # Edge weights visualization
        edge_weights = [
            max(0.1, min(5, subgraph[u][v][0].get('weight', 0.1) * 2))  # Adjust edge thickness with bounds
            for u, v in subgraph.edges()
        ]
        
        # Draw nodes and edges
        nx.draw_networkx_nodes(
            subgraph, pos, 
            node_color=node_colors, 
            node_size=node_sizes, 
            alpha=0.8,
            edgecolors='black',  # Add black outline to nodes
            linewidths=0.5
        )
        nx.draw_networkx_edges(
            subgraph, pos, 
            edge_color='gray', 
            width=edge_weights,
            alpha=0.5, 
            arrows=True,
            connectionstyle='arc3,rad=0.1'  # Curved edges for better visibility
        )
        
        # Improved label drawing
        nx.draw_networkx_labels(
            subgraph, pos, 
            font_size=8, 
            font_weight="bold",
            font_color='black',
            bbox=dict(
                facecolor='white', 
                edgecolor='lightgray', 
                boxstyle='round,pad=0.2', 
                alpha=0.7
            )
        )
        
        plt.title("Campaign Knowledge Graph (Edge Weights)", fontsize=20, fontweight='bold')
        plt.axis('off')
        
        # Save or show
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Graph visualization saved to {output_path}")
        else:
            plt.show()
        
        plt.close()
