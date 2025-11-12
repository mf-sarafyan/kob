from pathlib import Path

CONTENT_DIR = Path("content")
INDEX_DIR = Path(".rag_index")
LLM_MODEL = "llama3-groq-tool-use"
EMBED_MODEL = "openai/text-embedding-3-small"
CHUNK_SIZE = 600
CHUNK_OVERLAP = 100
TOP_K = 10


