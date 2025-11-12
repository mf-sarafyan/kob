import os
import json
import logging
from typing import List, Dict, Any, Optional

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import umap
import networkx as nx

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from .graph.graph_analysis import GraphAnalyzer
from .graph.graph_builder import ObsidianGraphBuilder
from .graph.text_processing import normalize_entity_name

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RAGAnalyzer:
    """
    Comprehensive analyzer for Retrieval-Augmented Generation (RAG) systems
    combining graph and vector database analysis.
    """
    
    def __init__(
        self, 
        vector_store: FAISS, 
        graph_builder: ObsidianGraphBuilder,
        output_dir: str = '.rag_index'
    ):
        """
        Initialize RAG analyzer with vector store and graph builder
        
        :param vector_store: FAISS vector store
        :param graph_builder: Obsidian graph builder
        :param output_dir: Directory to save analysis outputs
        """
        self.vector_store = vector_store
        self.graph_builder = graph_builder
        self.graph_analyzer = GraphAnalyzer(graph_builder.graph)
        self.output_dir = output_dir
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
    
    def visualize_vector_space(
        self, 
        output_filename: str = 'vector_space_projection.png',
        n_neighbors: int = 15,
        min_dist: float = 0.1
    ):
        """
        Create a 2D visualization of the vector space using UMAP
        
        :param output_filename: Name of the output image file
        :param n_neighbors: UMAP parameter for local neighborhood size
        :param min_dist: UMAP parameter for minimum distance between points
        """
        # Extract embeddings and metadata
        embeddings = self.vector_store.index.reconstruct_n(0, self.vector_store.index.ntotal)
        
        # Prepare lists for visualization
        node_labels = []
        node_types = []
        parent_entities = []
        
        # Retrieve documents from the vector store
        docs = list(self.vector_store.docstore._dict.values())
        
        for doc in docs:
            # Extract labels and metadata
            node_type = doc.metadata.get('graph_node_type', 'unknown')
            node_types.append(node_type)
            
            # Prioritize parent entity, fallback to source filename
            parent_entity = doc.metadata.get('parent_entity', 'unknown')
            if parent_entity == 'unknown':
                # Try to extract meaningful name from source
                source = doc.metadata.get('source', 'unknown')
                parent_entity = os.path.splitext(os.path.basename(source))[0]
            
            parent_entities.append(parent_entity)
            
            # Create a concise label
            label = parent_entity
            node_labels.append(label)
        
        # Dimensionality Reduction with UMAP
        reducer = umap.UMAP(
            n_components=2, 
            n_neighbors=n_neighbors, 
            min_dist=min_dist, 
            random_state=42
        )
        embedding_2d = reducer.fit_transform(embeddings)
        
        # Visualization
        plt.figure(figsize=(24, 18))
        
        # Color mapping for node types
        unique_node_types = list(set(node_types))
        color_palette = sns.color_palette("husl", len(unique_node_types))
        color_map = dict(zip(unique_node_types, color_palette))
        
        # Scatter plot
        for node_type in unique_node_types:
            mask = [nt == node_type for nt in node_types]
            plt.scatter(
                embedding_2d[mask, 0], 
                embedding_2d[mask, 1], 
                c=[color_map[node_type]], 
                label=node_type, 
                alpha=0.7
            )
        
        # Add labels for each point
        for i, label in enumerate(node_labels):
            plt.annotate(
                label, 
                (embedding_2d[i, 0], embedding_2d[i, 1]), 
                xytext=(3, 3),
                textcoords='offset points', 
                fontsize=4, 
                alpha=0.7,
                color='black'
            )
        
        plt.title("2D Projection of Vector Database", fontsize=20)
        plt.xlabel("UMAP Dimension 1", fontsize=16)
        plt.ylabel("UMAP Dimension 2", fontsize=16)
        plt.legend(title="Node Types", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        
        # Save the plot
        output_path = os.path.join(self.output_dir, output_filename)
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        # Print statistics
        logger.info(f"Vector space projection saved to {output_path}")
        logger.info(f"Total Vectors: {len(embeddings)}")
        
        # Node type distribution
        type_counts = {}
        for nt in node_types:
            type_counts[nt] = type_counts.get(nt, 0) + 1
        
        logger.info("\nNode Type Distribution:")
        for node_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
            logger.info(f"- {node_type}: {count} vectors")
        
        return type_counts
    
    def query_performance_analysis(
        self, 
        queries: List[str], 
        top_k: int = 5
    ) -> Dict[str, Dict[str, Any]]:
        """
        Analyze query performance across different types of queries
        
        :param queries: List of test queries
        :param top_k: Number of top results to retrieve
        :return: Dictionary of query performance metrics
        """
        query_results = {}
        
        for query in queries:
            # Perform vector similarity search
            docs = self.vector_store.similarity_search(query, k=top_k)
            
            # Analyze retrieved documents
            node_types = []
            parent_entities = []
            
            for doc in docs:
                node_type = doc.metadata.get('graph_node_type', 'unknown')
                parent_entity = doc.metadata.get('parent_entity', 'unknown')
                
                node_types.append(node_type)
                parent_entities.append(parent_entity)
            
            # Compute node type distribution
            type_counts = {}
            for nt in node_types:
                type_counts[nt] = type_counts.get(nt, 0) + 1
            
            query_results[query] = {
                'node_types': type_counts,
                'parent_entities': list(set(parent_entities)),
                'documents': [doc.page_content[:200] + '...' for doc in docs]
            }
        
        return query_results
    
    def graph_vector_correlation(self) -> Dict[str, Any]:
        """
        Analyze correlation between graph structure and vector space
        
        :return: Dictionary of correlation metrics
        """
        # Compute graph centrality measures
        centrality_measures = {
            'degree_centrality': nx.degree_centrality(self.graph_builder.graph),
            'betweenness_centrality': nx.betweenness_centrality(self.graph_builder.graph),
            'closeness_centrality': nx.closeness_centrality(self.graph_builder.graph)
        }
        
        # Compute embeddings for all nodes
        node_embeddings = {}
        for node_name in self.graph_builder.graph.nodes():
            # Find content chunks for this node
            content_chunks = [
                doc for doc in self.vector_store.docstore._dict.values()
                if doc.metadata.get('parent_entity') == node_name
            ]
            
            # Average embeddings for content chunks
            if content_chunks:
                chunk_embeddings = []
                for i in range(self.vector_store.index.ntotal):
                    try:
                        doc = self.vector_store.docstore._dict.get(i)
                        if doc in content_chunks:
                            chunk_embeddings.append(
                                self.vector_store.index.reconstruct(i)[0]
                            )
                    except Exception as e:
                        logger.warning(f"Could not retrieve embedding for {i}: {e}")
                
                if chunk_embeddings:
                    node_embeddings[node_name] = np.mean(chunk_embeddings, axis=0)
        
        # Compute correlations between centrality and embedding properties
        correlation_analysis = {
            'node_types_with_embeddings': list(node_embeddings.keys()),
            'total_nodes_with_embeddings': len(node_embeddings)
        }
        
        # Optional: Add more advanced correlation metrics
        try:
            # Compute cosine similarity between centrality and embedding spaces
            centrality_values = [
                centrality_measures['degree_centrality'].get(node, 0) 
                for node in node_embeddings.keys()
            ]
            
            # Compute embedding norms as a proxy for "importance"
            embedding_norms = [
                np.linalg.norm(emb) 
                for emb in node_embeddings.values()
            ]
            
            # Compute correlation
            correlation, p_value = scipy.stats.pearsonr(centrality_values, embedding_norms)
            
            correlation_analysis.update({
                'centrality_embedding_correlation': correlation,
                'correlation_p_value': p_value
            })
        except Exception as e:
            logger.warning(f"Could not compute advanced correlation metrics: {e}")
        
        return correlation_analysis
    
    def export_analysis_report(
        self, 
        output_filename: str = 'rag_analysis_report.json'
    ):
        """
        Export a comprehensive analysis report
        
        :param output_filename: Name of the output JSON file
        """
        # Collect analysis data
        report = {
            'vector_space': {
                'total_vectors': self.vector_store.index.ntotal,
                'vector_dimension': self.vector_store.index.d,
                'node_type_distribution': self.visualize_vector_space()
            },
            'graph_structure': {
                'total_nodes': len(self.graph_builder.graph.nodes),
                'total_edges': len(self.graph_builder.graph.edges),
                'node_type_distribution': self.graph_analyzer.count_nodes_by_type(),
                'most_connected_nodes': self.graph_analyzer.find_most_connected_nodes(top_k=10)
            },
            'graph_vector_correlation': self.graph_vector_correlation(),
            'query_performance': self.query_performance_analysis([
                "Who are the main characters in the party?",
                "What is the Rock of Bral?",
                "Tell me about the Spelljammer ships"
            ])
        }
        
        # Export to JSON
        output_path = os.path.join(self.output_dir, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Analysis report exported to {output_path}")
        return report

def create_rag_analyzer(
    content_dir: str, 
    index_dir: str, 
    chunk_size: int = 500, 
    chunk_overlap: int = 100, 
    embed_model: str = 'snowflake/snowflake-arctic-embed-l-v2.0'
) -> 'RAGAnalyzer':
    """
    Convenience function to create a RAG analyzer
    
    :param content_dir: Directory containing content
    :param index_dir: Directory to store index
    :param chunk_size: Size of text chunks
    :param chunk_overlap: Overlap between chunks
    :param embed_model: Embedding model to use
    :return: Configured RAG Analyzer
    """
    from .index import create_rag_index
    
    # Create RAG index
    vector_store, graph_builder, _ = create_rag_index(
        content_dir, 
        index_dir, 
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap, 
        embed_model=embed_model
    )
    
    # Create and return RAG analyzer
    return RAGAnalyzer(vector_store, graph_builder, index_dir)

# Example usage in __main__
if __name__ == '__main__':
    from src.settings import CONTENT_DIR, INDEX_DIR
    
    # Create RAG analyzer
    rag_analyzer = create_rag_analyzer(CONTENT_DIR, INDEX_DIR)
    
    # Run comprehensive analysis
    rag_analyzer.export_analysis_report()
    rag_analyzer.visualize_vector_space()
