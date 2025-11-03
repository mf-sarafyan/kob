import os
import logging
from typing import List, Dict, Any, Optional, Tuple

import networkx as nx
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings

from .graph.graph_builder import ObsidianGraphBuilder
from .graph.graph_analysis import GraphAnalyzer

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class VectorSearchAugmenter:
    """
    A tool that performs vector search and augments results with graph context
    """
    
    def __init__(
        self, 
        vector_store: FAISS, 
        graph_builder: ObsidianGraphBuilder,
        top_k: int = 5
    ):
        """
        Initialize the Vector Search Augmenter
        
        :param vector_store: FAISS vector store
        :param graph_builder: Obsidian graph builder
        :param top_k: Number of top results to retrieve
        """
        self.vector_store = vector_store
        self.graph_builder = graph_builder
        self.graph_analyzer = GraphAnalyzer(graph_builder.graph)
        self.top_k = top_k
    
    def search(
        self, 
        query: str, 
        return_type: str = 'entities'
    ) -> List[Dict[str, Any]]:
        """
        Perform vector search and augment results
        
        :param query: Search query
        :param return_type: 'entities' or 'documents'
        :return: List of entities or documents
        """
        # Perform vector similarity search
        docs = self.vector_store.similarity_search(query, k=self.top_k)
        
        # Collect unique parent entities
        parent_entities = set()
        entity_details = {}
        
        for doc in docs:
            parent_entity = doc.metadata.get('parent_entity', 'unknown')
            if parent_entity != 'unknown':
                parent_entities.add(parent_entity)
                
                # Collect entity details from graph
                if parent_entity not in entity_details:
                    try:
                        entity_node = self.graph_builder.graph.nodes.get(parent_entity, {})
                        entity_details[parent_entity] = {
                            'name': parent_entity,
                            'type': entity_node.get('type', 'unknown'),
                            'details': {
                                k: v for k, v in entity_node.items()
                                if k not in ['type', 'content']
                            },
                            'related_documents': []
                        }
                    except Exception as e:
                        logger.warning(f"Could not retrieve details for {parent_entity}: {e}")
                
                # Add document to entity's related documents
                if parent_entity in entity_details:
                    entity_details[parent_entity]['related_documents'].append({
                        'content': doc.page_content,
                        'source': doc.metadata.get('source', 'unknown'),
                        'chunk_id': doc.metadata.get('chunk_id', -1)
                    })
        
        # Return based on return type
        if return_type == 'entities':
            return list(entity_details.values())
        else:
            return docs


# Example usage in __main__
if __name__ == '__main__':
    from src.settings import CONTENT_DIR, INDEX_DIR
    from src.rag.index import create_rag_index
    
    # Create RAG index
    vector_store, graph_builder, _ = create_rag_index(CONTENT_DIR, INDEX_DIR)
    
    # Create vector search augmenter
    vector_search_augmenter = VectorSearchAugmenter(
        vector_store, 
        graph_builder, 
        top_k=5
    )
    
    # Example usage
    print("=== Vector Search Example ===")
    vector_results = vector_search_augmenter.search("Where is the rock of Bral?")
    print(vector_results)
