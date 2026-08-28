import os
import logging
from typing import List, Dict, Any, Optional

import networkx as nx
import json

from langchain_core.documents import Document

# Try modern import first, fallback to older import
try:
    from langchain_openai import OpenAIEmbeddings
except ImportError:
    from langchain_community.embeddings import OpenAIEmbeddings

from .graph.graph_builder import create_graph_rag_index
from .bm25_store import build_or_load_bm25

# Try to import secrets, fallback to environment variable
try:
    from src.secrets import OPENROUTER_API_KEY
except ImportError:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_openrouter_embeddings(model: str, api_key: Optional[str] = None):
    """
    Create OpenAI-compatible embeddings using OpenRouter
    
    :param model: OpenRouter model identifier (e.g., "snowflake/snowflake-arctic-embed-l-v2.0")
    :param api_key: OpenRouter API key (defaults to OPENROUTER_API_KEY from secrets or env)
    :return: OpenAIEmbeddings instance configured for OpenRouter
    """
    # Get API key from parameter, secrets file, or environment variable
    api_key = api_key or OPENROUTER_API_KEY
    if not api_key:
        raise ValueError(
            "OpenRouter API key not found. Please set OPENROUTER_API_KEY in src/secrets.py "
            "or as an environment variable."
        )
    
    # OpenRouter uses OpenAI-compatible API, so we use OpenAIEmbeddings with base_url
    return OpenAIEmbeddings(
        model=model,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        default_headers={
            "HTTP-Referer": "https://github.com/mf-sarafyan/kob",  
            "X-Title": "KEEPERS Campaign Knowledge Base"  
        }
    )

def create_rag_index(
    content_dir: str, 
    index_dir: str, 
    chunk_size: int = 500, 
    chunk_overlap: int = 100, 
    embed_model: str = 'snowflake/snowflake-arctic-embed-l-v2.0',
    api_key: Optional[str] = None
):
    """
    Create a comprehensive RAG index with BM25 lexical retrieval and graph components.

    :param content_dir: Directory containing content
    :param index_dir: Directory to store index
    :param chunk_size: Size of text chunks
    :param chunk_overlap: Overlap between chunks
    :param embed_model: Unused; kept for backward compatibility with callers
    :param api_key: Unused; kept for backward compatibility with callers
    :return: Tuple of (document_store, graph_builder, graph_path) — document_store exposes similarity_search like FAISS
    """
    # Ensure index directory exists
    os.makedirs(index_dir, exist_ok=True)
    
    # Create graph index first
    graph_builder = create_graph_rag_index(content_dir, index_dir)
    graph = graph_builder.graph
    
    # Load and chunk content from graph content nodes
    content_chunks = []
    for node_name, node_data in graph.nodes(data=True):
        # Only process content chunk nodes
        if node_data.get('type') == 'content_chunk':
            # Get parent entity
            parent_entity = node_data.get('parent_entity', 'unknown')
            
            # Get parent node details
            parent_node = graph.nodes.get(parent_entity, {})
            
            # Create document
            doc = Document(
                page_content=node_data.get('content', ''),
                metadata={
                    'source': node_data.get('file_path', 'unknown'),
                    'parent_entity': parent_entity,
                    'chunk_id': node_data.get('chunk_index', -1),
                    'graph_node_type': parent_node.get('type', 'unknown'),
                    'graph_node_details': {
                        k: v for k, v in parent_node.items() 
                        if k not in ['type', 'file_path', 'content']
                    }
                }
            )
            
            content_chunks.append(doc)
    
    # Lexical BM25 index (stronger exact / proper-noun matching than embedding similarity)
    vector_store = build_or_load_bm25(content_chunks, index_dir)
    
    # Export graph path for later use
    graph_path = os.path.join(index_dir, 'campaign_graph.json')
    
    return vector_store, graph_builder, graph_path


