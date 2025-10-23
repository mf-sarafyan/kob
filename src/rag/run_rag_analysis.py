#!/usr/bin/env python3
import sys
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.settings import CONTENT_DIR, INDEX_DIR
from src.rag.analysis import create_rag_analyzer

def main():
    """
    Run comprehensive RAG analysis
    """
    try:
        print("=== Running Comprehensive RAG Analysis ===")
        
        # Create RAG analyzer with BGE-M3 embedding model
        rag_analyzer = create_rag_analyzer(
            CONTENT_DIR, 
            INDEX_DIR, 
            embed_model='bge-m3'
        )
        
        # Visualize vector space
        print("\n1. Visualizing Vector Space...")
        vector_type_distribution = rag_analyzer.visualize_vector_space()
        
        # Export analysis report
        print("\n2. Generating Analysis Report...")
        report = rag_analyzer.export_analysis_report()
        
        # Query performance analysis
        print("\n3. Analyzing Query Performance...")
        queries = [
            "Who are the main characters in the party?",
            "What is the Rock of Bral?", 
            "Tell me about the Spelljammer ships"
        ]
        query_performance = rag_analyzer.query_performance_analysis(queries)
        
        # Print query performance details
        print("\nQuery Performance Details:")
        for query, results in query_performance.items():
            print(f"\nQuery: {query}")
            print("Node Types:", results['node_types'])
            print("Parent Entities:", results['parent_entities'])
            print("Document Previews:")
            for i, doc in enumerate(results['documents'], 1):
                print(f"  {i}. {doc}")
        
        print("\n=== RAG Analysis Complete ===")
        
    except Exception as e:
        logger.error(f"An error occurred during RAG analysis: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
