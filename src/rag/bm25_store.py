import os
import re
import pickle
import logging
from typing import List, Optional

from langchain_core.documents import Document
from rank_bm25 import BM25Okapi

logger = logging.getLogger(__name__)

# Word tokens: Unicode letters, digits, apostrophes (proper nouns, fantasy names)
_TOKEN_RE = re.compile(r"[\w']+", re.UNICODE)


def tokenize_for_bm25(text: str) -> List[str]:
    return _TOKEN_RE.findall(text.lower())


class BM25DocumentStore:
    """
    Lexical retrieval with BM25Okapi. Exposes similarity_search(query, k) like FAISS
    for drop-in use with VectorSearchAugmenter and chain helpers.
    """

    def __init__(self, documents: List[Document], bm25: Optional[BM25Okapi]):
        self.documents = documents
        self._bm25 = bm25

    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        tokens = tokenize_for_bm25(query)
        if not self.documents or self._bm25 is None:
            return []
        if not tokens:
            return self.documents[:k]

        scores = self._bm25.get_scores(tokens)
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        top = [i for i in ranked[:k] if scores[i] > 0]
        if not top:
            # No lexical overlap: return first k chunks so callers still get something
            return self.documents[:k]
        return [self.documents[i] for i in top]


def _validate_chunks(chunks: List) -> List[Document]:
    validated: List[Document] = []
    for chunk in chunks:
        if not hasattr(chunk, "metadata") or not isinstance(chunk.metadata, dict):
            chunk.metadata = {}
        for key in ("graph_node_type", "parent_entity", "source", "chunk_id"):
            if key not in chunk.metadata:
                chunk.metadata[key] = "unknown"
        validated.append(chunk)
    return validated


def build_or_load_bm25(chunks: List, index_dir: str) -> BM25DocumentStore:
    """
    Build or load a persisted BM25 index over document chunks.

    :param chunks: LangChain Document chunks
    :param index_dir: Base index directory (same as FAISS-era layout parent)
    :return: BM25DocumentStore
    """
    os.makedirs(index_dir, exist_ok=True)
    bm25_dir = os.path.join(index_dir, "bm25_index")
    os.makedirs(bm25_dir, exist_ok=True)
    state_path = os.path.join(bm25_dir, "bm25_state.pkl")

    if os.path.exists(state_path):
        logger.info("Loading existing BM25 index...")
        with open(state_path, "rb") as f:
            payload = pickle.load(f)
        return BM25DocumentStore(documents=payload["documents"], bm25=payload["bm25"])

    logger.info("Building new BM25 index...")
    validated = _validate_chunks(list(chunks))
    if not validated:
        store = BM25DocumentStore(documents=[], bm25=None)
        with open(state_path, "wb") as f:
            pickle.dump({"documents": [], "bm25": None}, f, protocol=pickle.HIGHEST_PROTOCOL)
        return store

    tokenized = [tokenize_for_bm25(doc.page_content or "") for doc in validated]
    bm25 = BM25Okapi(tokenized)
    store = BM25DocumentStore(documents=validated, bm25=bm25)

    with open(state_path, "wb") as f:
        pickle.dump({"documents": validated, "bm25": bm25}, f, protocol=pickle.HIGHEST_PROTOCOL)

    return store
