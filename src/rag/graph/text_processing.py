import re
import unicodedata
import html
import json
from typing import Dict, List, Any, Optional

def normalize_unicode(text: str, form: str = 'NFKC') -> str:
    """
    Normalize Unicode text to handle various character representations
    
    :param text: Input text to normalize
    :param form: Unicode normalization form (default: NFKC)
                 NFKC: Normalization Form Compatibility Composition
                 - Decomposes characters, then recomposes them
                 - Handles compatibility equivalents
    :return: Normalized text
    """
    # Ensure input is a string
    text = str(text)
    
    # Decode HTML entities
    text = html.unescape(text)
    
    # Normalize Unicode
    normalized = unicodedata.normalize(form, text)
    
    # Remove control characters using a more compatible method
    # This regex removes characters in Unicode control character categories
    normalized = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', normalized)
    
    # Preserve accented characters by replacing combining characters
    # This helps with characters like é, ó, ã that might be decomposed
    preserved_chars = []
    for char in normalized:
        # Get the category of the character
        category = unicodedata.category(char)
        
        # Keep letters, numbers, punctuation, and symbols
        if category.startswith(('L', 'N', 'P', 'S')):
            preserved_chars.append(char)
        # Keep spaces and whitespace
        elif category == 'Zs':
            preserved_chars.append(' ')
    
    # Join the preserved characters
    return ''.join(preserved_chars).strip()

def normalize_entity_name(name: str) -> str:
    """
    Normalize entity names by:
    1. Converting to lowercase
    2. Removing/replacing special characters
    3. Handling Unicode normalization
    4. Replacing spaces with underscores
    
    :param name: Original entity name
    :return: Normalized entity name
    """
    # Normalize Unicode
    normalized = normalize_unicode(name)
    
    # Convert to lowercase
    normalized = normalized.lower()
    
    # Replace multiple spaces with single space
    normalized = re.sub(r'\s+', ' ', normalized)
    
    # Replace spaces with underscores
    normalized = normalized.replace(' ', '_')
    
    # Remove any remaining non-alphanumeric characters except underscores
    normalized = re.sub(r'[^a-z0-9_]', '', normalized)
    
    # Ensure not empty
    return normalized if normalized else 'unnamed'

def clean_markdown_content(content: str) -> str:
    """
    Clean markdown content by:
    1. Removing frontmatter
    2. Handling Unicode normalization
    3. Removing excessive whitespace
    4. Removing dynamic blocks and comments
    5. Preserving important formatting
    
    :param content: Raw markdown content
    :return: Cleaned markdown content
    """
    # Ensure input is a string
    content = str(content)
    
    # Remove frontmatter if present
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).strip()
    
    # Remove dynamic blocks (Obsidian-specific and custom dynamic content)
    # Matches patterns like:
    # <!--DYNAMIC:something-->content<!--/DYNAMIC-->
    # {% dynamic block %}content{% enddynamic %}
    # [[dynamic:something]]
    dynamic_block_patterns = [
        r'<!--\s*DYNAMIC:.*?-->.*?<!--\s*/DYNAMIC\s*-->',  # HTML-style dynamic blocks
        r'{%\s*dynamic:.*?%}.*?{%\s*enddynamic\s*%}',     # Liquid-style dynamic blocks
        r'\[\[dynamic:.*?\]\]',                           # Wiki-style dynamic links
        r'<!--.*?-->',                                    # Remove all HTML comments
    ]
    
    for pattern in dynamic_block_patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Normalize Unicode
    content = normalize_unicode(content)
    
    # Remove excessive whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Trim leading and trailing whitespace
    content = content.strip()
    
    return content

def smart_chunk_content(content: str, max_chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """
    Intelligently chunk content while preserving semantic meaning
    
    :param content: Full content to chunk
    :param max_chunk_size: Maximum size of each chunk
    :param overlap: Number of characters to overlap between chunks
    :return: List of content chunks
    """
    # Normalize content
    content = normalize_unicode(content)
    
    # If content is shorter than max chunk size, return as single chunk
    if len(content) <= max_chunk_size:
        return [content]
    
    # Split content into paragraphs first
    paragraphs = content.split('\n\n')
    
    chunks = []
    current_chunk = []
    current_length = 0
    
    for paragraph in paragraphs:
        # If adding this paragraph would exceed max chunk size, start a new chunk
        if current_length + len(paragraph) > max_chunk_size:
            # Join current chunk and add to chunks
            chunks.append('\n\n'.join(current_chunk))
            
            # Start new chunk with overlap
            if len(chunks) > 0:
                current_chunk = [chunks[-1][-overlap:]]
                current_length = len(current_chunk[0])
            else:
                current_chunk = []
                current_length = 0
        
        # Add paragraph to current chunk
        current_chunk.append(paragraph)
        current_length += len(paragraph) + 2  # +2 for \n\n
    
    # Add final chunk if not empty
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks

def extract_headers(content: str) -> List[Dict[str, Any]]:
    """
    Extract headers from markdown content
    
    :param content: Markdown content
    :return: List of header dictionaries
    """
    # Normalize content
    content = normalize_unicode(content)
    
    # Regex to match markdown headers (ATX style)
    header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
    
    headers = []
    for match in header_pattern.finditer(content):
        header_level = len(match.group(1))
        header_text = match.group(2).strip()
        
        headers.append({
            'level': header_level,
            'text': header_text,
            'normalized_text': normalize_entity_name(header_text)
        })
    
    return headers
