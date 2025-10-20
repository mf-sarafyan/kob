import os
import re
from pathlib import Path
from typing import List, Dict, Any

import yaml
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def clean_markdown_content(content: str) -> str:
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

def extract_frontmatter(file_path: Path) -> Dict[str, Any]:
    """
    Extract YAML frontmatter from a Markdown file
    
    :param file_path: Path to the Markdown file
    :return: Dictionary of frontmatter properties
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Use regex to extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            try:
                frontmatter = yaml.safe_load(frontmatter_match.group(1)) or {}
                
                # Ensure type is set, derive from directory if not present
                if 'type' not in frontmatter:
                    path_parts = str(file_path).split(os.path.sep)
                    for part in path_parts:
                        if part in ['character', 'faction', 'location', 'item', 'entry', 'party']:
                            frontmatter['type'] = part
                            break
                
                return frontmatter
            except yaml.YAMLError:
                return {}
        return {}
    except Exception as e:
        print(f"Error extracting frontmatter from {file_path}: {e}")
        return {}

def load_and_chunk(
    content_dir: str, 
    chunk_size: int = 600, 
    chunk_overlap: int = 100
) -> List[Document]:
    """
    Load and chunk documents from the content directory
    
    :param content_dir: Directory containing markdown files
    :param chunk_size: Size of text chunks
    :param chunk_overlap: Overlap between chunks
    :return: List of document chunks
    """
    # Prepare text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    
    # Collect all documents
    documents = []
    processed_files = set()
    
    # Directories to search for markdown files
    search_dirs = [
        '1 Keepers\' Compendium/wiki/character', 
        '1 Keepers\' Compendium/wiki/faction', 
        '1 Keepers\' Compendium/wiki/location', 
        '1 Keepers\' Compendium/wiki/item', 
        '1 Keepers\' Compendium/wiki/entry',
        '1 Keepers\' Compendium/game/party'
    ]
    
    # Search for markdown files
    for subdir in search_dirs:
        dir_path = Path(content_dir) / subdir
        
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
            
            try:
                # Read file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
                
                # Extract frontmatter
                frontmatter = extract_frontmatter(file_path)
                
                # Clean content
                cleaned_content = clean_markdown_content(raw_content)
                
                # Skip empty files
                if not cleaned_content:
                    continue
                
                # Chunk the content
                chunks = text_splitter.split_text(cleaned_content)
                
                # Create documents with metadata
                for i, chunk in enumerate(chunks):
                    doc_metadata = {
                        'source': str(file_path),
                        'type': frontmatter.get('type', 'unknown'),
                        'chunk_id': i,
                        **frontmatter
                    }
                    
                    documents.append(
                        Document(
                            page_content=chunk, 
                            metadata=doc_metadata
                        )
                    )
            
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    print(f"Loaded {len(documents)} document chunks")
    return documents


