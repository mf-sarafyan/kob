"""
Player's Handbook agent (LangChain example).

For editors and assistants, prefer the MCP server, which exposes the same search
without embedding a full agent here::

    python -m src.mcp_servers.server_phb

This module reuses :mod:`src.mcp_servers.phb_service` so behavior matches the MCP tool.
"""
import os

try:
    from src.secrets import OPENROUTER_API_KEY
except ImportError:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from src.mcp_servers.phb_service import search_phb


@tool
def get_context_from_phb(query: str) -> str:
    """
    Search the D&D 5.5e Player's Handbook PDF for context related to a query.

    Performs BM25 lexical search and returns relevant excerpts with citations.
    """
    return search_phb(query, k=3)


def build_phb_agent():
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )
    return create_agent(
        model=llm,
        system_prompt=(
            "You are a helpful assistant with expertise on the Dungeons and Dragons 5e Player's Handbook. "
            "Answer from the PHB context returned by tools. When you state rules or numbers, cite the source "
            "the tool gave you (book title and page, e.g. Player's Handbook (2024) p. 94)."
        ),
        tools=[get_context_from_phb],
    )


if __name__ == "__main__":
    import pprint

    agent = build_phb_agent()
    result1 = agent.invoke(
        {"messages": [{"role": "user", "content": "How do I grapple someone? What does it do?"}]}
    )
    pprint.pp(result1)
