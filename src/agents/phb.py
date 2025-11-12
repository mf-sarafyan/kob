import os

# Try to import secrets, fallback to environment variable
try:
    from src.secrets import OPENROUTER_API_KEY
except ImportError:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")


# PHB Context
phb_file = "D:\\DnD\\1 - Campaign - THE KEEPERS\\kob\\content\\1 Keepers' Compendium\\rules\\Books\\DnD 5.5e - Players Handbook 2024 - PHOTOSCAN2OCR.pdf"

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain.tools import tool

# Load and chunk PHB PDF (do this once for all requests)
_loader = PyPDFLoader(phb_file)
_documents = _loader.load()
_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
_phb_chunks = _splitter.split_documents(_documents)

from langchain_community.vectorstores import FAISS
from src.rag.index import create_openrouter_embeddings

# Create embeddings instance using the same function as graph/RAG code
# Uses the default embed model from settings (snowflake/snowflake-arctic-embed-l-v2.0)
from src.settings import EMBED_MODEL
_phb_embeddings = create_openrouter_embeddings(model=EMBED_MODEL, api_key=OPENROUTER_API_KEY)

# Build FAISS vector store for PHB, or load if already exists
import tempfile
_phb_index_dir = os.path.join(tempfile.gettempdir(), "kob_phb_faiss")
os.makedirs(_phb_index_dir, exist_ok=True)
_faiss_index_path = os.path.join(_phb_index_dir, "faiss_phb")
if os.path.exists(_faiss_index_path):
    phb_vectorstore = FAISS.load_local(_faiss_index_path, _phb_embeddings, allow_dangerous_deserialization=True)
else:
    phb_vectorstore = FAISS.from_documents(_phb_chunks, _phb_embeddings)
    phb_vectorstore.save_local(_faiss_index_path)

@tool
def get_context_from_phb(query: str) -> str:
    """
    Search the D&D 5.5e Player's Handbook PDF for context related to a query.
    
    Performs a semantic search and returns relevant excerpts.
    """
    # Perform similarity search
    results = phb_vectorstore.similarity_search(query, k=3)
    if not results:
        return "No relevant information found in the Player's Handbook for your query."
    excerpts = []
    for i, doc in enumerate(results, 1):
        page = doc.metadata.get('page', None)
        page_str = f" (page {page+1})" if page is not None else ""
        excerpts.append(f"[Excerpt {i}{page_str}]: {doc.page_content.strip()[:600]}")
    return "\n\n".join(excerpts)

# Chat/agent setup

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from langchain.tools import tool

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

agent = create_agent(
    model=llm,
    system_prompt = "Your are a helpful assistant with expertise on the Dungeons and Dragons 5e Player's Handbook. Answer user questions based on the PHB.",
    tools=[get_context_from_phb],
    )

# Testing
import pprint

# result1 = agent.invoke({"messages": [{"role": "user", "content": "How does grappling work?"}]})
# pprint.pp(result1)

# result2 = agent.invoke({"messages": [{"role": "user", "content": "Explain Line of Sight rules"}]})
# pprint.pp(result2)

# result2 = agent.invoke({"messages": [{"role": "user", "content": "I just got to level 5 as a wizard, can you suggest some spells to learn?"}]})
# pprint.pp(result2)

result2 = agent.invoke({"messages": [{"role": "user", "content": "What are some good expertise options for a Rogue?"}]})
pprint.pp(result2)