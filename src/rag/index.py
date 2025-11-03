import os
import logging
from typing import List, Dict, Any, Optional

import networkx as nx
import json

from langchain.docstore.document import Document
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

from .graph.graph_builder import create_graph_rag_index

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def build_or_load_faiss(chunks: List, index_dir: str, embed_model: str):
    """
    Build or load a FAISS vector store
    
    :param chunks: List of document chunks
    :param index_dir: Directory to store/load index
    :param embed_model: Embedding model to use
    :return: FAISS vector store
    """
    # Ensure index directory exists
    os.makedirs(index_dir, exist_ok=True)
    
    # Path for vector store
    faiss_index_path = os.path.join(index_dir, 'faiss_index')
    
    # Check if index already exists
    if os.path.exists(faiss_index_path):
        print("Loading existing FAISS index...")
        embedding = OllamaEmbeddings(model=embed_model)
        
        # Load the vector store
        vector_store = FAISS.load_local(faiss_index_path, embedding, allow_dangerous_deserialization=True)
        
        return vector_store
    
    # Create embeddings
    print(f"Creating new FAISS index with {embed_model} embeddings...")
    embedding = OllamaEmbeddings(model=embed_model)
    
    # Validate and prepare chunks
    validated_chunks = []
    for chunk in chunks:
        # Ensure each chunk has a complete metadata dictionary
        if not hasattr(chunk, 'metadata') or not isinstance(chunk.metadata, dict):
            chunk.metadata = {}
        
        # Ensure critical metadata keys exist
        metadata_keys = [
            'graph_node_type', 
            'parent_entity', 
            'source', 
            'chunk_id'
        ]
        for key in metadata_keys:
            if key not in chunk.metadata:
                chunk.metadata[key] = 'unknown'
        
        validated_chunks.append(chunk)
    
    # Build vector store with validated chunks
    vector_store = FAISS.from_documents(validated_chunks, embedding)
    
    # Save the index
    vector_store.save_local(faiss_index_path)
    
    return vector_store

def create_rag_index(
    content_dir: str, 
    index_dir: str, 
    chunk_size: int = 500, 
    chunk_overlap: int = 100, 
    embed_model: str = 'bge-m3'  # Updated default embedding model
):
    """
    Create a comprehensive RAG index with vector and graph components
    
    :param content_dir: Directory containing content
    :param index_dir: Directory to store index
    :param chunk_size: Size of text chunks
    :param chunk_overlap: Overlap between chunks
    :param embed_model: Embedding model to use
    :return: Tuple of (vector_store, graph_builder, graph_path)
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
    
    # Create vector store
    vector_store = build_or_load_faiss(content_chunks, index_dir, embed_model)
    
    # Export graph path for later use
    graph_path = os.path.join(index_dir, 'campaign_graph.json')
    
    return vector_store, graph_builder, graph_path


