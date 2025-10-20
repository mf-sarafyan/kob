import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.settings import (
    CONTENT_DIR, 
    INDEX_DIR, 
    LLM_MODEL, 
    EMBED_MODEL, 
    CHUNK_SIZE, 
    CHUNK_OVERLAP, 
    TOP_K
)

from src.rag.index import create_rag_index
from src.rag.chain import make_graph_rag_chain

def main():
    """
    Main application entry point for RAG system
    """
    print("Initializing RAG System...")
    
    # Create RAG index (vector store and graph)
    vector_store, graph_builder, graph_path = create_rag_index(
        content_dir=CONTENT_DIR,
        index_dir=INDEX_DIR,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        embed_model=EMBED_MODEL
    )
    
    # Create graph-enhanced RAG chain
    rag_chain = make_graph_rag_chain(
        vector_store=vector_store, 
        graph_path=graph_path, 
        llm_model=LLM_MODEL, 
        top_k=TOP_K
    )
    
    # Interactive query loop
    print("\nGraph-Enhanced RAG System Ready!")
    print("Type 'exit' to quit.")
    
    while True:
        try:
            # Get user query
            query = input("\nEnter your query: ").strip()
            
            # Exit condition
            if query.lower() in ['exit', 'quit', 'q']:
                print("Exiting...")
                break
            
            # Run RAG query
            result = rag_chain({"query": query})
            
            # Display result
            print("\n--- RAG Response ---")
            print(result["result"])
            
            # Display sources
            print("\n--- Sources ---")
            for i, doc in enumerate(result.get("source_documents", []), 1):
                print(f"{i}. {Path(doc.metadata.get('source', '')).name}")
                print(f"   Graph Context: {doc.metadata.get('graph_context', {})}")
        
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


