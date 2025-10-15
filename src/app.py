import streamlit as st
from pathlib import Path
from src.settings import CONTENT_DIR, INDEX_DIR, LLM_MODEL, EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP, TOP_K
from src.rag.load import load_and_chunk
from src.rag.index import build_or_load_faiss
from src.rag.chain import make_rag_chain


@st.cache_resource(show_spinner=True)
def get_chain():
    chunks = load_and_chunk(CONTENT_DIR, CHUNK_SIZE, CHUNK_OVERLAP)
    vs = build_or_load_faiss(chunks, INDEX_DIR, EMBED_MODEL)
    return make_rag_chain(vs, LLM_MODEL, TOP_K)


def main():
    st.set_page_config(page_title="Keepers RAG Chat", page_icon="🧭")
    st.title("Keepers RAG Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("Ask about the compendium…")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Retrieving…"):
            chain = get_chain()
            result = chain({"query": user_input})
            answer = result["result"]
            sources = result.get("source_documents", [])
        st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            if msg["role"] == "assistant" and msg.get("sources"):
                with st.expander("Sources"):
                    for i, doc in enumerate(msg["sources"], 1):
                        st.caption(f"{i}. {Path(doc.metadata.get('source','')).name} — p:{doc.metadata.get('page', 'n/a')}")


if __name__ == "__main__":
    main()


