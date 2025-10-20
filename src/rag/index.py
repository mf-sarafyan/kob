from pathlib import Path
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import time
import logging
import hashlib
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Any

import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

from .graph import create_graph_rag_index
from .load import load_and_chunk

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def compute_chunks_hash(chunks):
    """
    Compute a hash of chunk contents to detect changes.
    
    Args:
        chunks (List[Document]): List of document chunks
    
    Returns:
        str: Hash of chunk contents
    """
    # Extract unique identifiable information from chunks
    chunk_identifiers = [
        (
            chunk.metadata.get('source', ''), 
            chunk.page_content[:500]  # First 500 chars to reduce computation
        ) for chunk in chunks
    ]
    
    # Convert to string and hash
    hash_input = json.dumps(chunk_identifiers, sort_keys=True)
    return hashlib.md5(hash_input.encode()).hexdigest()

def parallel_embed_chunks(chunks: List[Any], embeddings, max_workers: int = 4) -> List[List[float]]:
    """
    Embed chunks in parallel using ThreadPoolExecutor.
    
    Args:
        chunks (List[Any]): List of document chunks
        embeddings (OllamaEmbeddings): Embedding model
        max_workers (int): Maximum number of worker threads
    
    Returns:
        List[List[float]]: List of embedding vectors
    """
    logger.info(f"Starting parallel embedding with {max_workers} workers")
    start_time = time.time()
    
    def embed_chunk(chunk):
        """Embed a single chunk"""
        try:
            # Combine entity context with page content for embedding
            entity_context = chunk.metadata.get('entity_context', '')
            text_to_embed = f"{entity_context}\n\n{chunk.page_content}"
            return embeddings.embed_query(text_to_embed)
        except Exception as e:
            logger.error(f"Embedding error: {e}")
            return None
    
    # Use ThreadPoolExecutor for parallel embedding
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit embedding jobs
        future_to_chunk = {
            executor.submit(embed_chunk, chunk): chunk 
            for chunk in chunks
        }
        
        # Collect results
        embeddings_list = []
        failed_chunks = 0
        for future in as_completed(future_to_chunk):
            result = future.result()
            if result is not None:
                embeddings_list.append(result)
            else:
                failed_chunks += 1
    
    embedding_time = time.time() - start_time
    logger.info(f"Parallel embedding completed in {embedding_time:.2f} seconds")
    logger.info(f"Total embeddings: {len(embeddings_list)}, Failed: {failed_chunks}")
    
    return embeddings_list

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
        vector_store = FAISS.load_local(faiss_index_path, embedding, allow_dangerous_deserialization=True)
        return vector_store
    
    # Create embeddings
    print(f"Creating new FAISS index with {embed_model} embeddings...")
    embedding = OllamaEmbeddings(model=embed_model)
    
    # Build vector store
    vector_store = FAISS.from_documents(chunks, embedding)
    
    # Save the index
    vector_store.save_local(faiss_index_path)
    
    return vector_store

def create_rag_index(content_dir: str, index_dir: str, chunk_size: int, chunk_overlap: int, embed_model: str):
    """
    Create a comprehensive RAG index with vector and graph components
    
    :param content_dir: Directory containing content
    :param index_dir: Directory to store index
    :param chunk_size: Size of text chunks
    :param chunk_overlap: Overlap between chunks
    :param embed_model: Embedding model to use
    :return: Tuple of (vector_store, graph_builder)
    """
    # Ensure index directory exists
    os.makedirs(index_dir, exist_ok=True)
    
    # Create graph index first
    graph_builder = create_graph_rag_index(content_dir, index_dir)
    
    # Load and chunk content
    chunks = load_and_chunk(content_dir, chunk_size, chunk_overlap)
    
    # Enhance chunks with graph metadata
    enhanced_chunks = []
    for chunk in chunks:
        # Find the parent entity for this chunk
        parent_entity = chunk.metadata.get('parent_entity', chunk.metadata.get('source', '').split('/')[-1].split('.')[0])
        
        # Try to get node details from the graph
        node_details = graph_builder.graph.nodes.get(parent_entity, {})
        
        # Update chunk metadata with graph information
        chunk.metadata.update({
            'graph_node_type': node_details.get('type', 'unknown'),
            'graph_node_details': {k: v for k, v in node_details.items() if k not in ['type', 'file_path', 'content']}
        })
        
        enhanced_chunks.append(chunk)
    
    # Create vector store
    vector_store = build_or_load_faiss(enhanced_chunks, index_dir, embed_model)
    
    # Export graph path for later use
    graph_path = os.path.join(index_dir, 'campaign_graph.json')
    
    return vector_store, graph_builder, graph_path


