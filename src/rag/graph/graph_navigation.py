import logging
from typing import Dict, List, Any, Optional

import networkx as nx

from .text_processing import normalize_entity_name

logger = logging.getLogger(__name__)

class GraphNavigator:
    """
    Provides navigation and search utilities for the knowledge graph
    """
    def __init__(self, graph: nx.MultiDiGraph):
        """
        Initialize the graph navigator
        
        :param graph: NetworkX MultiDiGraph to navigate
        """
        self.graph = graph
    
    def resolve_node(self, search_term: str) -> Optional[str]:
        """
        Resolve a search term to its primary node, handling aliases and variations
        
        :param search_term: Search term to resolve
        :return: Primary node name, or None if not found
        """
        # Normalize the search term
        normalized_search = normalize_entity_name(search_term)
        
        # Direct node name match
        if normalized_search in self.graph.nodes:
            return normalized_search
        
        # Check for alias nodes
        alias_node = f"alias_{normalized_search}"
        if alias_node in self.graph.nodes:
            # Retrieve the original entity from the alias node
            return self.graph.nodes[alias_node].get('original_entity')
        
        # If no match found, return None
        return None
    
    def find_node_by_name_or_alias(self, search_term: str) -> List[Dict[str, Any]]:
        """
        Find nodes by exact name, partial name, or alias
        
        :param search_term: Term to search for
        :return: List of matching nodes with their details
        """
        matching_nodes = []
        
        # Normalize search term
        normalized_search = normalize_entity_name(search_term)
        
        for node, node_data in self.graph.nodes(data=True):
            # Check for direct node matches or alias matches
            is_match = (
                node == normalized_search or 
                normalize_entity_name(node_data.get('title', '')) == normalized_search or
                (node_data.get('type') == 'alias' and 
                 normalize_entity_name(node_data.get('alias_of', '')) == normalized_search)
            )
            
            if is_match:
                # If it's an alias, get the original entity details
                if node_data.get('type') == 'alias':
                    original_node = node_data.get('original_entity')
                    if original_node:
                        original_node_data = dict(self.graph.nodes[original_node])
                        original_node_data['alias_info'] = node_data
                        matching_nodes.append({
                            'node': original_node,
                            'type': original_node_data.get('type', 'unknown'),
                            'details': original_node_data
                        })
                else:
                    matching_nodes.append({
                        'node': node,
                        'type': node_data.get('type', 'unknown'),
                        'details': dict(node_data)
                    })
        
        return matching_nodes
    
    def get_node_content(self, node_name: str) -> Dict[str, Any]:
        """
        Retrieve comprehensive content for a node
        
        :param node_name: Name of the node to retrieve content for
        :return: Dictionary with node content details
        """
        # Resolve node name (handle aliases)
        resolved_node = self.resolve_node(node_name) or node_name
        
        if resolved_node not in self.graph.nodes:
            return {"error": f"Node '{node_name}' not found in the graph"}
        
        # Get main node data
        node_data = dict(self.graph.nodes[resolved_node])
        
        # Prepare comprehensive entity details
        entity_details = {
            "node_name": resolved_node,
            "node_type": node_data.get('type', 'unknown'),
            "node_attributes": {},
            "content": {
                "content_chunks": []
            },
            "connections": {
                "incoming": [],
                "outgoing": []
            }
        }
        
        # Add main_content only if it exists in the node itself (for content_chunk nodes)
        # Main entity nodes don't store content directly - it's in content_chunk nodes
        if 'content' in node_data and node_data.get('type') != 'content_chunk':
            entity_details['content']['main_content'] = node_data.get('content', '')
        
        # Add all node attributes (excluding content and type)
        for key, value in node_data.items():
            if key not in ['content', 'type']:
                entity_details['node_attributes'][key] = value
        
        # Find and sort content chunks - get all chunks connected via 'has_content_chunk' edges
        content_chunks = []
        for _, target, edge_data in self.graph.out_edges(resolved_node, data=True):
            if edge_data.get('type') == 'has_content_chunk':
                # Get chunk node data as a proper dict
                chunk_node_data = dict(self.graph.nodes[target])
                
                # Verify this is actually a content_chunk node
                if chunk_node_data.get('type') == 'content_chunk':
                    content_chunks.append(chunk_node_data)
        
        # Sort content chunks by index
        content_chunks.sort(key=lambda x: x.get('chunk_index', 0))
        
        # Add sorted content chunks with all their fields
        chunk_contents = []
        for chunk_node in content_chunks:
            chunk_content = chunk_node.get('content', '')
            if chunk_content:  # Only add non-empty chunks
                chunk_contents.append(chunk_content)
            
            entity_details['content']['content_chunks'].append({
                'chunk_index': chunk_node.get('chunk_index', -1),
                'content': chunk_content,
                'file_path': chunk_node.get('file_path', 'Unknown'),
                'parent_entity': chunk_node.get('parent_entity', resolved_node)
            })
        
        # Combine all chunks into full_content for easier consumption
        if chunk_contents:
            entity_details['content']['full_content'] = '\n\n'.join(chunk_contents)
        elif 'main_content' in entity_details['content']:
            entity_details['content']['full_content'] = entity_details['content'].get('main_content', '')
        else:
            entity_details['content']['full_content'] = ''
        
        # Collect incoming connections
        for source, _, edge_data in self.graph.in_edges(resolved_node, data=True):
            entity_details['connections']['incoming'].append({
                'source_node': source,
                'source_type': self.graph.nodes[source].get('type', 'unknown'),
                'edge_type': edge_data.get('type', 'unknown'),
                'weight': edge_data.get('weight', 0)
            })
        
        # Collect outgoing connections (exclude content_chunk nodes - they're handled separately)
        for _, target, edge_data in self.graph.out_edges(resolved_node, data=True):
            target_type = self.graph.nodes[target].get('type', 'unknown')
            edge_type = edge_data.get('type', 'unknown')
            
            # Skip content_chunk nodes - they're part of content, not semantic connections
            if target_type != 'content_chunk' and edge_type != 'has_content_chunk':
                entity_details['connections']['outgoing'].append({
                    'target_node': target,
                    'target_type': target_type,
                    'edge_type': edge_type,
                    'weight': edge_data.get('weight', 0)
                })
        
        return entity_details
    
    def get_related_nodes(self, node_name: str, max_depth: int = 2) -> Dict[str, Any]:
        """
        Find related nodes for a given entity
        
        :param node_name: Name of the starting node
        :param max_depth: Maximum depth of exploration
        :return: Dictionary of related nodes
        """
        # Resolve node name (handle aliases)
        resolved_node = self.resolve_node(node_name) or node_name
        
        if resolved_node not in self.graph.nodes:
            return {"error": f"Node '{node_name}' not found in the graph"}
        
        # Prepare exploration results
        related_nodes = {
            "direct_connections": {},
            "indirect_connections": {}
        }
        
        # Direct connections (1-hop) - exclude content_chunk nodes
        for neighbor in self.graph.neighbors(resolved_node):
            neighbor_type = self.graph.nodes[neighbor].get('type', 'unknown')
            
            # Skip content_chunk nodes - they're part of content structure, not semantic connections
            if neighbor_type != 'content_chunk':
                edge_data = list(self.graph.get_edge_data(resolved_node, neighbor).values())[0]
                edge_type = edge_data.get('type', 'unknown')
                
                # Also skip has_content_chunk edges
                if edge_type != 'has_content_chunk':
                    related_nodes["direct_connections"][neighbor] = {
                        "type": neighbor_type,
                        "edge_type": edge_type,
                        "edge_weight": edge_data.get('weight', 0)
                    }
        
        # Indirect connections (2-hop)
        if max_depth > 1:
            start_node_type = self.graph.nodes[resolved_node].get('type', 'unknown')
            for neighbor in related_nodes["direct_connections"].keys():
                for indirect_neighbor in self.graph.neighbors(neighbor):
                    # Only add indirect connections of the same type as the starting node
                    if (indirect_neighbor != resolved_node and 
                        self.graph.nodes[indirect_neighbor].get('type') == start_node_type):
                        related_nodes["indirect_connections"][indirect_neighbor] = {
                            "type": self.graph.nodes[indirect_neighbor].get('type', 'unknown'),
                            "via": neighbor
                        }
        
        return related_nodes
