import re
from typing import List, Dict, Any
from pathlib import Path
import yaml
import json

class ObsidianRelationExtractor:
    def __init__(self):
        # Regex for extracting frontmatter
        self.frontmatter_pattern = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
        
        # Regex patterns for wikilinks
        self.wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')

    def extract_frontmatter(self, text: str) -> Dict[str, Any]:
        """
        Extract YAML frontmatter from Obsidian markdown file.
        
        Args:
            text (str): Full text of the markdown file
        
        Returns:
            Dict[str, Any]: Parsed frontmatter
        """
        frontmatter_match = self.frontmatter_pattern.search(text)
        if frontmatter_match:
            try:
                return yaml.safe_load(frontmatter_match.group(1)) or {}
            except yaml.YAMLError:
                return {}
        return {}

    def extract_wikilinks(self, text: str) -> List[str]:
        """
        Extract all wikilinks from a text.
        
        Args:
            text (str): Text to extract wikilinks from
        
        Returns:
            List[str]: List of unique wikilinks
        """
        return list(set(self.wikilink_pattern.findall(text)))

    def generate_entity_context(self, metadata: Dict[str, Any], wikilinks: List[str]) -> str:
        """
        Generate a context string from metadata.
        
        Args:
            metadata (Dict[str, Any]): Parsed frontmatter metadata
            wikilinks (List[str]): Extracted wikilinks
        
        Returns:
            str: Formatted metadata string
        """
        # Convert metadata to a readable string
        metadata_parts = []
        
        # Add all metadata key-value pairs
        for key, value in metadata.items():
            # Convert list values to comma-separated strings
            if isinstance(value, list):
                value = ', '.join(map(str, value))
            
            metadata_parts.append(f"{key}: {value}")
        
        # Add wikilinks if not already in metadata
        if wikilinks and 'wikilinks' not in metadata:
            metadata_parts.append(f"Related Entities: {', '.join(wikilinks)}")
        
        return " | ".join(metadata_parts)

def preprocess_documents(documents):
    """
    Preprocess documents to enhance their metadata with Obsidian-specific information.
    
    Args:
        documents (List[Document]): List of langchain documents
    
    Returns:
        List[Document]: Documents with enhanced metadata
    """
    extractor = ObsidianRelationExtractor()
    
    for doc in documents:
        # Extract frontmatter
        frontmatter = extractor.extract_frontmatter(doc.page_content)
        
        # Update metadata with frontmatter
        doc.metadata.update(frontmatter)
        
        # Extract wikilinks
        wikilinks = extractor.extract_wikilinks(doc.page_content)
        doc.metadata['wikilinks'] = wikilinks
        
        # Generate entity context
        doc.metadata['entity_context'] = extractor.generate_entity_context(
            doc.metadata, 
            wikilinks
        )
    
    return documents

# Simplified backlink tracking
class BacklinkTracker:
    def __init__(self):
        self.backlinks = {}
    
    def track_backlinks(self, documents):
        """
        Track basic backlinks across documents.
        
        Args:
            documents (List[Document]): List of documents to track backlinks for
        
        Returns:
            Dict[str, List[str]]: Mapping of entities to documents linking to them
        """
        # Reset backlinks
        self.backlinks = {}
        
        # Iterate through documents to find backlinks
        for doc in documents:
            wikilinks = doc.metadata.get('wikilinks', [])
            source = doc.metadata.get('source', 'Unknown')
            
            for link in wikilinks:
                if link not in self.backlinks:
                    self.backlinks[link] = []
                self.backlinks[link].append(source)
        
        return self.backlinks
