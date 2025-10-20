import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

import networkx as nx
import yaml
import json
import matplotlib.pyplot as plt
import unicodedata

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

class ObsidianGraphBuilder:
    def __init__(self, content_dir: str):
        """
        Initialize the graph builder for Obsidian notes
        
        :param content_dir: Root directory of Obsidian vault
        """
        self.content_dir = Path(content_dir)
        self.graph = nx.MultiDiGraph()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=600, 
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def _extract_frontmatter(self, file_path: Path) -> Dict[str, Any]:
        """
        Extract YAML frontmatter from a Markdown file
        
        :param file_path: Path to the Markdown file
        :return: Dictionary of frontmatter properties
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Use regex to extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            try:
                return yaml.safe_load(frontmatter_match.group(1)) or {}
            except yaml.YAMLError:
                return {}
        return {}
    
    def _extract_wikilinks(self, content: str) -> List[str]:
        """
        Extract Obsidian wikilinks from Markdown content
        
        :param content: Markdown content
        :return: List of wikilinks
        """
        # Regex to match Obsidian wikilinks [[Link]] or [[Link|Alias]]
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
        
        # Remove aliases and clean links
        cleaned_links = []
        for link in wikilinks:
            # Split on | to remove aliases
            base_link = link.split('|')[0].strip()
            
            # Ignore empty links
            if base_link:
                cleaned_links.append(base_link)
        
        return cleaned_links
    
    def _get_reciprocal_relationship(self, relationship_type: str) -> Optional[str]:
        """
        Get the reciprocal relationship type
        
        :param relationship_type: Original relationship type
        :return: Reciprocal relationship type or None
        """
        reciprocal_map = {
            'member_of': 'has_member',
            'child_of': 'parent_of',
            'parent_of': 'child_of',
            'originates_from': 'origin_of',
            'associated_with': 'associates',
            'appears_in': 'contains',
            'related_to': 'related_to'  # Symmetric relationship
        }
        
        return reciprocal_map.get(relationship_type)
    
    def _process_explicit_relationships(self, node_name: str, frontmatter: Dict[str, Any]):
        """
        Process and add explicit relationships defined in frontmatter
        
        :param node_name: Name of the current node
        :param frontmatter: Frontmatter dictionary
        """
        # Relationship mapping with weights and priorities
        relationship_weights = {
            'factions': {'type': 'member_of', 'weight': 0.9, 'reciprocal': 'has_member'},
            'parent': {'type': 'child_of', 'weight': 0.8, 'reciprocal': 'parent_of'},
            'children': {'type': 'parent_of', 'weight': 0.8, 'reciprocal': 'child_of'},
            'relates_to': {'type': 'related_to', 'weight': 0.5, 'reciprocal': 'related_to'},
            'origin': {'type': 'originates_from', 'weight': 0.6, 'reciprocal': 'origin_of'},
            'known_locations': {'type': 'associated_with', 'weight': 0.7, 'reciprocal': 'associates'},
            'appears_in': {'type': 'appears_in', 'weight': 0.4, 'reciprocal': 'contains'}
        }
        
        # Process each relationship type
        for key, rel_info in relationship_weights.items():
            if key in frontmatter and frontmatter[key]:
                # Ensure it's a list
                relationships = frontmatter[key]
                if isinstance(relationships, str):
                    relationships = [relationships]
                
                # Remove wikilink formatting and clean
                cleaned_relationships = []
                for rel in relationships:
                    # Remove wikilink formatting
                    cleaned_rel = rel.strip('[]').split('|')[0].strip()
                    if cleaned_rel:
                        cleaned_relationships.append(cleaned_rel)
                
                # Add edges for each relationship
                for related_node in cleaned_relationships:
                    # Normalize related node name
                    normalized_node = related_node.split('.')[0]
                    
                    # Ensure the related node exists in the graph
                    if normalized_node not in self.graph.nodes:
                        self.graph.add_node(normalized_node, type='unknown', file_path='')
                    
                    # Add forward edge
                    self.graph.add_edge(
                        node_name, 
                        normalized_node, 
                        type=rel_info['type'],
                        weight=rel_info.get('weight', 0.3)  # Default weight if not specified
                    )
                    
                    # Add reciprocal edge if a reciprocal type is defined
                    if 'reciprocal' in rel_info:
                        self.graph.add_edge(
                            normalized_node,
                            node_name,
                            type=rel_info['reciprocal'],
                            weight=rel_info.get('weight', 0.3) * 0.8  # Slightly reduced weight for reciprocal
                        )
    
    def _clean_markdown_content(self, content: str) -> str:
        """
        Clean markdown content by removing:
        1. Frontmatter
        2. Triple-backtick code blocks
        3. Dynamic sections
        4. Comments
        
        :param content: Raw markdown content
        :return: Cleaned content
        """
        # Remove frontmatter
        frontmatter_pattern = re.compile(r'^---\n.*?---\n', re.DOTALL)
        content = frontmatter_pattern.sub('', content)
        
        # Remove triple-backtick code blocks
        code_block_pattern = re.compile(r'```[\s\S]*?```', re.MULTILINE)
        content = code_block_pattern.sub('', content)
        
        # Remove dynamic sections (Obsidian-specific)
        dynamic_section_pattern = re.compile(r'<!--\s*DYNAMIC:.*?-->.*?<!--\s*\/DYNAMIC\s*-->', re.DOTALL)
        content = dynamic_section_pattern.sub('', content)
        
        # Remove HTML comments
        comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
        content = comment_pattern.sub('', content)
        
        # Remove extra whitespace
        content = re.sub(r'\n{3,}', '\n\n', content).strip()
        
        return content
    
    @staticmethod
    def normalize_entity_name(name: str) -> str:
        """
        Normalize entity names to handle special characters and encoding
        
        :param name: Original entity name
        :return: Normalized entity name
        """
        # Normalize Unicode characters
        normalized = unicodedata.normalize('NFKD', name)
        
        # Remove non-ASCII characters while preserving meaningful ones
        cleaned = ''.join(
            char for char in normalized 
            if unicodedata.category(char) != 'Mn'  # Remove combining characters
        )
        
        # Replace problematic characters
        cleaned = cleaned.replace('α', 'alpha').replace('β', 'beta')
        
        # Remove or replace any remaining non-printable characters
        cleaned = re.sub(r'[^\w\s-]', '', cleaned)
        
        return cleaned.strip()
    
    def explore_unknown_entities(self) -> Dict[str, Any]:
        """
        Explore and analyze unknown type entities in the graph
        
        :return: Detailed analysis of unknown entities
        """
        # Find unknown entities
        unknown_entities = [
            node for node, data in self.graph.nodes(data=True) 
            if data.get('type', 'unknown') == 'unknown'
        ]
        
        # Analyze unknown entities
        analysis = {
            "total_unknown_entities": len(unknown_entities),
            "potential_sources": {},
            "sample_entities": unknown_entities[:20]
        }
        
        # Track potential sources of unknown entities
        for entity in unknown_entities:
            # Find incoming edges to understand potential origin
            incoming_edges = list(self.graph.in_edges(entity, data=True))
            
            if incoming_edges:
                sources = {}
                for _, source, edge_data in incoming_edges:
                    source_type = self.graph.nodes[source].get('type', 'unknown')
                    sources[source] = {
                        "type": source_type,
                        "edge_type": edge_data.get('type', 'unknown')
                    }
                
                analysis["potential_sources"][entity] = sources
        
        return analysis
    
    def build_graph(self, wiki_subdirs: List[str] = None):
        """
        Build a graph from Obsidian notes
        
        :param wiki_subdirs: List of wiki subdirectories to process
        """
        if wiki_subdirs is None:
            wiki_subdirs = [
                '1 Keepers\' Compendium/wiki/character', 
                '1 Keepers\' Compendium/wiki/faction', 
                '1 Keepers\' Compendium/wiki/location', 
                '1 Keepers\' Compendium/wiki/item', 
                '1 Keepers\' Compendium/wiki/entry',
                '1 Keepers\' Compendium/game/party'  # Added party directory
            ]
        
        # Track processed files to avoid duplicates
        processed_files = set()
        
        for subdir in wiki_subdirs:
            dir_path = self.content_dir / subdir
            
            # Ensure directory exists
            if not dir_path.exists():
                print(f"Warning: Directory not found - {dir_path}")
                continue
            
            for file_path in dir_path.glob('*.md'):
                # Skip desktop.ini and other non-markdown files
                if file_path.name == 'desktop.ini':
                    continue
                
                # Avoid processing the same file multiple times
                if file_path in processed_files:
                    continue
                processed_files.add(file_path)
                
                # Read file content
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        raw_content = f.read()
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    continue
                
                # Extract node properties
                node_name = self.normalize_entity_name(file_path.stem)
                frontmatter = self._extract_frontmatter(file_path)
                wikilinks = self._extract_wikilinks(raw_content)
                
                # Determine node type (prefer frontmatter, fallback to directory)
                node_type = frontmatter.get('type')
                if not node_type:
                    # Derive type from directory path
                    path_parts = str(file_path).split(os.path.sep)
                    for part in path_parts:
                        if part in ['character', 'faction', 'location', 'item', 'entry', 'party']:
                            node_type = part
                            break
                
                # Clean and chunk content
                cleaned_content = self._clean_markdown_content(raw_content)
                content_chunks = self.text_splitter.split_text(cleaned_content)
                
                # Add node to graph
                node_attrs = {
                    'type': node_type or 'unknown',
                    'file_path': str(file_path),
                    **frontmatter
                }
                self.graph.add_node(node_name, **node_attrs)
                
                # Process explicit relationships from frontmatter
                self._process_explicit_relationships(node_name, frontmatter)
                
                # Add chunked content nodes
                for chunk_idx, chunk in enumerate(content_chunks):
                    # Create unique content node name
                    content_node_name = f"{node_name}_content_{chunk_idx}"
                    
                    # Add content chunk node
                    self.graph.add_node(content_node_name, 
                        type='content_chunk', 
                        parent_entity=node_name,
                        chunk_index=chunk_idx,
                        file_path=str(file_path),
                        content=chunk
                    )
                    
                    # Strong connection between entity and its content chunks
                    self.graph.add_edge(
                        node_name, 
                        content_node_name, 
                        type='has_content_chunk', 
                        weight=0.9  # Very strong connection
                    )
                    
                    # Connect adjacent content chunks
                    if chunk_idx > 0:
                        prev_content_node = f"{node_name}_content_{chunk_idx-1}"
                        self.graph.add_edge(
                            prev_content_node, 
                            content_node_name, 
                            type='adjacent_chunk', 
                            weight=0.7
                        )
                
                # Add edges for wikilinks (as secondary connections)
                for link in wikilinks:
                    # Normalize link (remove file extension if present)
                    normalized_link = self.normalize_entity_name(link.split('.')[0])
                    
                    # Check if link exists in graph, if not, create a placeholder node
                    if normalized_link not in self.graph.nodes:
                        self.graph.add_node(normalized_link, type='unknown', file_path='')
                    
                    # Add edge (with lower priority)
                    self.graph.add_edge(node_name, normalized_link, type='wikilink', weight=0.3)
        
        print(f"Graph built with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges")
        
        # Analyze and print relationship types
        edge_types = {}
        for _, _, data in self.graph.edges(data=True):
            edge_type = data.get('type', 'unknown')
            edge_types[edge_type] = edge_types.get(edge_type, 0) + 1
        
        print("\nRelationship Types:")
        for edge_type, count in sorted(edge_types.items(), key=lambda x: x[1], reverse=True):
            print(f"- {edge_type}: {count} edges")
        
        # Explore unknown entities
        unknown_analysis = self.explore_unknown_entities()
        print("\nUnknown Entities Analysis:")
        print(f"Total Unknown Entities: {unknown_analysis['total_unknown_entities']}")
        print("Sample Unknown Entities:")
        for entity in unknown_analysis['sample_entities']:
            print(f"- {entity}")
        
        return unknown_analysis
    
    def get_node_context(self, node_name: str, max_hops: int = 2) -> Dict[str, Any]:
        """
        Get contextual information about a node by exploring its neighborhood
        
        :param node_name: Name of the node
        :param max_hops: Maximum number of hops to explore
        :return: Dictionary of contextual information
        """
        if node_name not in self.graph.nodes:
            return {}
        
        # Get node's direct attributes
        node_data = dict(self.graph.nodes[node_name])
        
        # Explore neighborhood
        neighborhood = {
            'direct_connections': {},
            'indirect_connections': {}
        }
        
        # Direct neighbors (1-hop)
        for neighbor in self.graph.neighbors(node_name):
            neighborhood['direct_connections'][neighbor] = {
                'type': self.graph.nodes[neighbor].get('type', 'unknown'),
                'edge_types': list(set(data['type'] for _, _, data in self.graph.edges(node_name, neighbor, data=True)))
            }
        
        # Indirect neighbors (2-hop)
        if max_hops > 1:
            for neighbor in self.graph.neighbors(node_name):
                for indirect_neighbor in self.graph.neighbors(neighbor):
                    if indirect_neighbor != node_name:
                        neighborhood['indirect_connections'][indirect_neighbor] = {
                            'type': self.graph.nodes[indirect_neighbor].get('type', 'unknown'),
                            'via': neighbor
                        }
        
        return {
            'node_data': node_data,
            'neighborhood': neighborhood
        }
    
    def export_graph(self, output_path: Optional[str] = None):
        """
        Export the graph to a file or return a serializable representation
        
        :param output_path: Optional path to export the graph
        :return: Serializable graph representation
        """
        graph_data = nx.readwrite.json_graph.node_link_data(self.graph)
        
        if output_path:
            import json
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(graph_data, f, indent=2)
        
        return graph_data
    
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
        
        # Prepare exploration results
        exploration = {
            "node_name": node_name,
            "node_type": node_data.get('type', 'unknown'),
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
                    if indirect_neighbor != node_name:
                        exploration["connections"]["indirect"][indirect_neighbor] = {
                            "type": self.graph.nodes[indirect_neighbor].get('type', 'unknown'),
                            "via": neighbor
                        }
        
        return exploration
    
    def find_nodes_by_type(self, node_type: str) -> List[str]:
        """
        Find all nodes of a specific type
        
        :param node_type: Type of nodes to find
        :return: List of node names
        """
        return [
            node for node, data in self.graph.nodes(data=True) 
            if data.get('type') == node_type
        ]
    
    def get_strongest_connections(self, node_name: str, top_k: int = 5):
        """
        Find the strongest connections for a given node
        
        :param node_name: Name of the node to explore
        :param top_k: Number of top connections to return
        :return: List of strongest connected nodes with connection details
        """
        if node_name not in self.graph.nodes:
            return []
        
        # Get all edges for the node
        edges = list(self.graph.edges(node_name, data=True))
        
        # Sort edges by weight (descending)
        sorted_edges = sorted(
            edges, 
            key=lambda x: x[2].get('weight', 0), 
            reverse=True
        )
        
        # Prepare top connections
        top_connections = []
        for _, target, data in sorted_edges[:top_k]:
            connection_info = {
                'node': target,
                'type': data.get('type', 'unknown'),
                'weight': data.get('weight', 0),
                'node_type': self.graph.nodes[target].get('type', 'unknown')
            }
            top_connections.append(connection_info)
        
        return top_connections
    
    def visualize_graph(self, output_path: Optional[str] = None, max_nodes: int = 500):
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
        plt.figure(figsize=(30, 30))
        pos = nx.spring_layout(subgraph, k=0.5, iterations=50, seed=42)
        
        # Color mapping for node types
        type_colors = {
            'character': 'skyblue',
            'faction': 'lightgreen', 
            'location': 'salmon',
            'item': 'purple',
            'entry': 'orange',
            'party': 'pink',
            'unknown': 'gray'
        }
        
        # Node colors
        node_colors = [
            type_colors.get(subgraph.nodes[node].get('type', 'unknown'), 'gray') 
            for node in subgraph.nodes
        ]
        
        # Node sizes based on number of connections
        node_sizes = [
            100 + 10 * subgraph.degree(node) 
            for node in subgraph.nodes
        ]
        
        # Edge weights visualization
        edge_weights = [
            subgraph[u][v][0].get('weight', 0.1) * 2  # Adjust edge thickness
            for u, v in subgraph.edges()
        ]
        
        # Draw nodes and edges
        nx.draw_networkx_nodes(
            subgraph, pos, 
            node_color=node_colors, 
            node_size=node_sizes, 
            alpha=0.8
        )
        nx.draw_networkx_edges(
            subgraph, pos, 
            edge_color='gray', 
            width=edge_weights,
            alpha=0.5, 
            arrows=True
        )
        nx.draw_networkx_labels(
            subgraph, pos, 
            font_size=8, 
            font_weight="bold"
        )
        
        plt.title("Campaign Knowledge Graph (Edge Weights)")
        plt.axis('off')
        
        # Save or show
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Graph visualization saved to {output_path}")
        else:
            plt.show()
        
        plt.close()

    def get_bidirectional_connections(self, node_name: str):
        """
        Find bidirectional connections for a given node
        
        :param node_name: Name of the node to explore
        :return: List of bidirectional connections
        """
        if node_name not in self.graph.nodes:
            return []
        
        # Prepare bidirectional connections
        bidirectional_connections = []
        
        # Iterate through all neighbors
        for target in self.graph.neighbors(node_name):
            # Get all edges between node_name and target
            outgoing_edges = self.graph.get_edge_data(node_name, target, default={})
            incoming_edges = self.graph.get_edge_data(target, node_name, default={})
            
            # Convert to list of edge dictionaries if not already
            outgoing_edges_list = list(outgoing_edges.values()) if outgoing_edges else []
            incoming_edges_list = list(incoming_edges.values()) if incoming_edges else []
            
            # Check if there are reciprocal edges
            if outgoing_edges_list and incoming_edges_list:
                # Prepare connection details
                connection = {
                    'node': target,
                    'outgoing': {
                        'type': outgoing_edges_list[0].get('type', 'unknown'),
                        'weight': outgoing_edges_list[0].get('weight', 0)
                    },
                    'incoming': {
                        'type': incoming_edges_list[0].get('type', 'unknown'),
                        'weight': incoming_edges_list[0].get('weight', 0)
                    },
                    'node_type': self.graph.nodes[target].get('type', 'unknown')
                }
                bidirectional_connections.append(connection)
        
        return bidirectional_connections

    def get_entity_context(self, entity_name: str, max_depth: int = 2) -> Dict[str, Any]:
        """
        Get comprehensive context for an entity
        
        :param entity_name: Name of the entity to explore
        :param max_depth: Maximum depth of exploration
        :return: Detailed context dictionary
        """
        if entity_name not in self.graph.nodes:
            return {"error": f"Entity '{entity_name}' not found in graph"}
        
        # Prepare context dictionary
        context = {
            "entity_name": entity_name,
            "node_data": dict(self.graph.nodes[entity_name]),
            "connections": {
                "direct": {},
                "indirect": {}
            },
            "content_chunks": []
        }
        
        # Find direct connections
        for neighbor in self.graph.neighbors(entity_name):
            edge_data = list(self.graph.get_edge_data(entity_name, neighbor).values())[0]
            context["connections"]["direct"][neighbor] = {
                "type": edge_data.get('type', 'unknown'),
                "weight": edge_data.get('weight', 0),
                "node_type": self.graph.nodes[neighbor].get('type', 'unknown')
            }
        
        # Find content chunks
        content_chunks = [
            node for node in self.graph.nodes 
            if node.startswith(f"{entity_name}_content_")
        ]
        
        # Sort content chunks by index
        content_chunks.sort(key=lambda x: int(x.split('_')[-1]))
        
        # Add content chunks to context
        for chunk_node in content_chunks:
            context["content_chunks"].append({
                "node_name": chunk_node,
                "content": self.graph.nodes[chunk_node].get('content', ''),
                "chunk_index": self.graph.nodes[chunk_node].get('chunk_index', -1)
            })
        
        # Find indirect connections (2-hop)
        if max_depth > 1:
            for neighbor in context["connections"]["direct"].keys():
                for indirect_neighbor in self.graph.neighbors(neighbor):
                    if indirect_neighbor != entity_name:
                        context["connections"]["indirect"][indirect_neighbor] = {
                            "type": self.graph.nodes[indirect_neighbor].get('type', 'unknown'),
                            "via": neighbor
                        }
        
        return context
    
    def find_related_entities(
        self, 
        entity_name: str, 
        relationship_types: List[str] = None, 
        max_depth: int = 2
    ) -> List[Dict[str, Any]]:
        """
        Find entities related to a given entity
        
        :param entity_name: Name of the starting entity
        :param relationship_types: List of relationship types to filter
        :param max_depth: Maximum depth of exploration
        :return: List of related entities with connection details
        """
        if entity_name not in self.graph.nodes:
            return []
        
        # If no relationship types specified, use all
        if relationship_types is None:
            relationship_types = ['member_of', 'child_of', 'parent_of', 'related_to', 
                                  'originates_from', 'associated_with', 'appears_in', 
                                  'wikilink']
        
        related_entities = []
        
        # Explore direct connections
        for neighbor in self.graph.neighbors(entity_name):
            # Get all edges between the nodes
            edges = self.graph.get_edge_data(entity_name, neighbor)
            
            for edge_data in edges.values():
                # Check if relationship type matches
                if edge_data.get('type') in relationship_types:
                    related_entity_info = {
                        "entity": neighbor,
                        "relationship_type": edge_data.get('type', 'unknown'),
                        "weight": edge_data.get('weight', 0),  # Default to 0 if no weight
                        "node_type": self.graph.nodes[neighbor].get('type', 'unknown')
                    }
                    related_entities.append(related_entity_info)
        
        # Explore indirect connections if max_depth > 1
        if max_depth > 1:
            indirect_related = []
            for direct_related in related_entities:
                # Find connections of the directly related entities
                for indirect_neighbor in self.graph.neighbors(direct_related['entity']):
                    if indirect_neighbor != entity_name:
                        indirect_related.append({
                            "entity": indirect_neighbor,
                            "relationship_type": f"indirect_{direct_related['relationship_type']}",
                            "via": direct_related['entity'],
                            "weight": 0.1,  # Low weight for indirect connections
                            "node_type": self.graph.nodes[indirect_neighbor].get('type', 'unknown')
                        })
            
            related_entities.extend(indirect_related)
        
        return related_entities
    
    def expand_context(
        self, 
        entity_name: str, 
        context_types: List[str] = None, 
        max_depth: int = 2
    ) -> Dict[str, Any]:
        """
        Expand context for an entity by exploring its connections
        
        :param entity_name: Name of the starting entity
        :param context_types: Types of entities to include in context
        :param max_depth: Maximum depth of exploration
        :return: Expanded context dictionary
        """
        if entity_name not in self.graph.nodes:
            return {"error": f"Entity '{entity_name}' not found in graph"}
        
        # If no context types specified, use all
        if context_types is None:
            context_types = ['character', 'faction', 'location', 'item', 'entry']
        
        # Get initial entity context
        expanded_context = self.get_entity_context(entity_name, max_depth)
        
        # Find related entities
        related_entities = {}
        for related in self.find_related_entities(entity_name, max_depth=max_depth):
            # Filter by node type
            if related['node_type'] in context_types:
                # Get detailed context for each related entity
                related_context = self.get_entity_context(related['entity'], max_depth=1)
                related_entities[related['entity']] = {
                    "connection": related,
                    "details": related_context
                }
        
        expanded_context['related_entities'] = related_entities
        
        return expanded_context

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

def create_graph_rag_index(content_dir: str, output_dir: str):
    """
    Create a graph-based RAG index
    
    :param content_dir: Directory containing Obsidian notes
    :param output_dir: Directory to store graph index
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Build the graph
    graph_builder = ObsidianGraphBuilder(content_dir)
    graph_builder.build_graph()
    
    # Export the graph
    graph_path = os.path.join(output_dir, 'campaign_graph.json')
    graph_builder.export_graph(graph_path)
    
    return graph_builder

# Example usage and interactive exploration
if __name__ == '__main__':
    from src.settings import CONTENT_DIR, INDEX_DIR
    
    # Create graph index
    graph_builder = create_graph_rag_index(CONTENT_DIR, INDEX_DIR)
    
    # Exploration functions
    def explore_entity(entity_name):
        print(f"\n--- Exploring Entity: {entity_name} ---")
        
        # Get entity context
        print("\n1. Entity Context:")
        context = graph_builder.get_entity_context(entity_name)
        print(json.dumps(context, indent=2))
        
        # Find related entities
        print("\n2. Related Entities:")
        related = graph_builder.find_related_entities(entity_name)
        for rel in related:
            print(f"- {rel['entity']} (Type: {rel['relationship_type']}, Weight: {rel['weight']:.2f})")
        
        # Expand context
        print("\n3. Expanded Context:")
        expanded = graph_builder.expand_context(entity_name)
        print(json.dumps({
            'direct_connections': list(expanded['connections']['direct'].keys()),
            'related_entities': list(expanded['related_entities'].keys())
        }, indent=2))
    
    # Graph-wide exploration
    def explore_graph_overview():
        print("\n--- Graph Overview ---")
        
        # Count nodes by type
        print("\n1. Node Type Counts:")
        type_counts = graph_builder.count_nodes_by_type()
        for node_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"- {node_type}: {count}")
        
        # Most connected nodes
        print("\n2. Most Connected Nodes:")
        most_connected = graph_builder.find_most_connected_nodes(top_k=10)
        for node in most_connected:
            print(f"- {node['node']} (Type: {node['type']}, Connections: {node['total_connections']})")
    
    # Interactive graph explorer
    def interactive_graph_explorer():
        while True:
            print("\n--- Graph Explorer ---")
            print("1. Explore an Entity")
            print("2. Graph Overview")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                entity = input("Enter entity name to explore: ").strip()
                try:
                    explore_entity(entity)
                except Exception as e:
                    print(f"Error exploring entity: {e}")
            
            elif choice == '2':
                explore_graph_overview()
            
            elif choice == '3':
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    # Run example explorations
    print("\n--- Example Explorations ---")
    
    # Explore Baang
    explore_entity('Baang')
    
    # Graph overview
    explore_graph_overview()
    
    # Interactive exploration
    interactive_graph_explorer()
