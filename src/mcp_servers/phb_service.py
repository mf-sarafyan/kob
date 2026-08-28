"""
Shared PHB PDF index and search (used by MCP server and optional LangChain wrappers).
"""
from __future__ import annotations

import logging
import os
import tempfile
from functools import lru_cache

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.rag.bm25_store import build_or_load_bm25
from src.rag.citations import format_sourced_text_block
from src.settings import PHB_PDF_PATH

logger = logging.getLogger(__name__)

PHB_BOOK_TITLE = "Player's Handbook (2024)"


@lru_cache(maxsize=1)
def _phb_vectorstore():
    path = str(PHB_PDF_PATH)
    if not os.path.isfile(path):
        raise FileNotFoundError(
            f"PHB PDF not found at {path}. Set KOB_PHB_PDF or place the file under the repo content path."
        )
    logger.info("Loading PHB PDF for BM25 index…")
    loader = PyPDFLoader(path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(documents)
    index_dir = os.path.join(tempfile.gettempdir(), "kob_phb_bm25")
    os.makedirs(index_dir, exist_ok=True)
    return build_or_load_bm25(chunks, index_dir)


def search_phb(query: str, k: int = 3) -> str:
    """
    BM25 search over the Player's Handbook; returns sourced excerpt blocks.
    """
    store = _phb_vectorstore()
    results = store.similarity_search(query, k=k)
    if not results:
        return "No relevant information found in the Player's Handbook for your query."
    excerpts = [
        format_sourced_text_block(
            doc.page_content,
            doc.metadata,
            max_chars=600,
            title_override=PHB_BOOK_TITLE,
        )
        for doc in results
    ]
    return "\n\n---\n\n".join(excerpts)
