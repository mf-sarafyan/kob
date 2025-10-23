import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

import networkx as nx
import yaml
import json

from .text_processing import normalize_entity_name, clean_markdown_content, smart_chunk_content

class ObsidianGraphBuilder:
    def __init__(self, content_dir: str):
        """
        Initialize the graph builder for Obsidian notes
        
        :param content_dir: Root directory of Obsidian vault
        """
        self.content_dir = Path(content_dir)
        self.graph = nx.MultiDiGraph()
    
    def _extract_frontmatter(self, file_path: Path) -> Dict[str, Any]:
        """
        Extract frontmatter from a markdown file
        
        :param file_path: Path to the markdown file
        :return: Dictionary of frontmatter key-value pairs
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Use yaml to parse frontmatter
            frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            
            if frontmatter_match:
                frontmatter_str = frontmatter_match.group(1)
                frontmatter = yaml.safe_load(frontmatter_str) or {}
                
                # Normalize aliases
                if 'aliases' in frontmatter:
                    # Ensure aliases is a list
                    aliases = frontmatter['aliases']
                    if isinstance(aliases, str):
                        aliases = [aliases]
                    frontmatter['aliases'] = [str(alias) for alias in aliases]
                
                return frontmatter
            
            return {}
        
        except Exception as e:
            logger.warning(f"Could not extract frontmatter from {file_path}: {e}")
            return {}
    
    def _process_node(self, file_path: Path) -> Optional[str]:
        """
        Process a single file into a graph node
        
        :param file_path: Path to the markdown file
        :return: Name of the created node, or None if failed
        """
        try:
            # Extract frontmatter
            frontmatter = self._extract_frontmatter(file_path)
            
            # Determine node name and type
            node_name = frontmatter.get('title') or file_path.stem
            node_type = frontmatter.get('type', 'note')
            
            # Normalize node name
            normalized_name = normalize_entity_name(node_name)
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove frontmatter
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).strip()
            
            # Clean markdown content
            cleaned_content = clean_markdown_content(content)
            
            # Prepare node attributes
            node_attrs = {
                'type': node_type,
                'file_path': str(file_path),
                'content': cleaned_content,
                'title': node_name,
            }
            
            # Add aliases from frontmatter
            aliases = frontmatter.get('aliases', [])
            if aliases:
                node_attrs['aliases'] = aliases
            
            # Add other frontmatter attributes
            for key, value in frontmatter.items():
                if key not in ['title', 'type', 'aliases']:
                    node_attrs[key] = value
            
            # Add node to graph
            self.graph.add_node(normalized_name, **node_attrs)
            
            return normalized_name
        
        except Exception as e:
            logger.error(f"Error processing node from {file_path}: {e}")
            return None
    
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
                node_name = normalize_entity_name(file_path.stem)
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
                cleaned_content = clean_markdown_content(raw_content)
                content_chunks = smart_chunk_content(cleaned_content)
                
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
                    normalized_link = normalize_entity_name(link.split('.')[0])
                    
                    # Check if link exists in graph, if not, create a placeholder node
                    if normalized_link not in self.graph.nodes:
                        self.graph.add_node(normalized_link, type='unknown', file_path='')
                    
                    # Add edge (with lower priority)
                    self.graph.add_edge(node_name, normalized_link, type='wikilink', weight=0.3)
        
        print(f"Graph built with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges")
        
        return self.graph

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
    graph = graph_builder.build_graph()
    
    # Export the graph
    graph_path = os.path.join(output_dir, 'campaign_graph.json')
    graph_data = nx.readwrite.json_graph.node_link_data(graph)
    
    with open(graph_path, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, indent=2)
    
    return graph_builder
