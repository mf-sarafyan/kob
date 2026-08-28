import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIR = Path("content")
INDEX_DIR = Path(".rag_index")

# Player's Handbook PDF (override with env KOB_PHB_PDF)
_default_phb = (
    REPO_ROOT
    / "content"
    / "1 Keepers' Compendium"
    / "rules"
    / "Books"
    / "DnD 5.5e - Players Handbook 2024 - PHOTOSCAN2OCR.pdf"
)
PHB_PDF_PATH = Path(os.environ.get("KOB_PHB_PDF", str(_default_phb)))
LLM_MODEL = "llama3-groq-tool-use"
EMBED_MODEL = "openai/text-embedding-3-small"
CHUNK_SIZE = 600
CHUNK_OVERLAP = 100
TOP_K = 10


