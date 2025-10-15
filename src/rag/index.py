from pathlib import Path
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def build_or_load_faiss(chunks, index_dir: Path, embed_model: str):
    # Ensure index directory exists
    index_dir.mkdir(parents=True, exist_ok=True)
    faiss_path = index_dir / "faiss_index"

    # Log the embedding model being used
    logger.info(f"Using embedding model: {embed_model}")
    logger.info(f"Index directory: {index_dir}")
    logger.info(f"Total chunks to process: {len(chunks)}")

    # Initialize embeddings
    start_time = time.time()
    try:
        embeddings = OllamaEmbeddings(model=embed_model)
        logger.info("Embeddings initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize embeddings: {e}")
        raise

    # Check if index already exists
    if faiss_path.exists():
        logger.info(f"Existing FAISS index found at {faiss_path}")
        try:
            start_load_time = time.time()
            vs = FAISS.load_local(
                folder_path=str(faiss_path),
                embeddings=embeddings,
                allow_dangerous_deserialization=True,
            )
            load_time = time.time() - start_load_time
            logger.info(f"Loaded existing FAISS index in {load_time:.2f} seconds")
            return vs
        except Exception as e:
            logger.warning(f"Failed to load existing index: {e}. Will rebuild.")

    # Build new FAISS index
    logger.info("Building new FAISS index...")
    try:
        start_build_time = time.time()
        
        # Validate chunks
        if not chunks:
            logger.error("No chunks provided to build FAISS index")
            raise ValueError("Cannot build FAISS index with empty chunks")

        # Build vector store
        vs = FAISS.from_documents(chunks, embedding=embeddings)
        
        # Save the index
        vs.save_local(str(faiss_path))
        
        build_time = time.time() - start_build_time
        total_time = time.time() - start_time
        
        logger.info(f"FAISS index built in {build_time:.2f} seconds")
        logger.info(f"Total time (including embeddings): {total_time:.2f} seconds")
        logger.info(f"Vector store created with {vs.index.ntotal} vectors")
        logger.info(f"Vector dimension: {vs.index.d}")
        
        return vs
    
    except Exception as e:
        logger.error(f"Failed to build FAISS index: {e}")
        raise


