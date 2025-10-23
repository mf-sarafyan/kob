import re
from typing import List, Dict, Any
import unicodedata

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

def extract_headers(content: str) -> List[Dict[str, Any]]:
    """
    Extract headers from markdown content with their levels and positions
    
    :param content: Markdown content
    :return: List of header dictionaries with level, text, and start position
    """
    # Regex to match markdown headers (ATX style)
    header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
    
    headers = []
    for match in header_pattern.finditer(content):
        headers.append({
            'level': len(match.group(1)),
            'text': match.group(2).strip(),
            'start': match.start(),
            'end': match.end()
        })
    
    return headers

def smart_chunk_content(
    content: str, 
    min_content_size: int = 400, 
    target_chunk_size: int = 500
) -> List[str]:
    """
    Chunk content intelligently, respecting headers and minimum content size
    
    :param content: Full markdown content
    :param min_content_size: Minimum content size before splitting
    :param target_chunk_size: Target chunk size
    :return: List of content chunks
    """
    # If content is too small, return as-is
    if len(content.split()) < min_content_size:
        return [content]
    
    # Extract headers
    headers = extract_headers(content)
    
    # If no headers, fall back to simple chunking
    if not headers:
        # Simple word-based chunking
        words = content.split()
        chunks = []
        current_chunk = []
        current_size = 0
        
        for word in words:
            current_chunk.append(word)
            current_size += 1
            
            if current_size >= target_chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_size = 0
        
        # Add remaining chunk
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    # Header-aware chunking
    chunks = []
    current_chunk = []
    current_chunk_size = 0
    
    # Iterate through content sections defined by headers
    for i in range(len(headers)):
        # Get the section content
        start = headers[i]['end']
        end = headers[i+1]['start'] if i+1 < len(headers) else len(content)
        section_content = content[start:end].strip()
        
        # If adding this section would exceed target size, start a new chunk
        if current_chunk_size + len(section_content.split()) > target_chunk_size:
            # Save current chunk
            if current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_chunk_size = 0
        
        # Add header to chunk
        current_chunk.append(f"{'#' * headers[i]['level']} {headers[i]['text']}")
        current_chunk.append(section_content)
        current_chunk_size += len(section_content.split()) + 1
    
    # Add final chunk if not empty
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

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
