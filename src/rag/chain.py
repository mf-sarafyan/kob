from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


SYSTEM_PROMPT = """You are a helpful lore assistant for the Dungeons & Dragons campaign 'Keepers of the Balance'.
Use ONLY the provided context. If the answer is not in the context, say you don't know.
Always cite sources by filename. Be concise and accurate.

Context:
{context}

Question: {question}
"""


def make_rag_chain(vectorstore, llm_model: str, top_k: int):
    retriever = vectorstore.as_retriever(search_kwargs={"k": top_k})
    llm = Ollama(model=llm_model, temperature=0.2)
    prompt = PromptTemplate.from_template(SYSTEM_PROMPT)
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )
    return chain


