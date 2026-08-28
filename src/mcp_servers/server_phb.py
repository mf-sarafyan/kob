"""
MCP server: D&D 5.5e Player's Handbook (BM25 search with page citations).

Run from repository root (so ``src`` is importable)::

    python -m src.mcp_servers.server_phb

Cursor / Claude Desktop: add an MCP server with command ``python``, args
``["-m", "src.mcp_servers.server_phb"]``, and ``cwd`` set to this repo.
"""
from __future__ import annotations

import logging

from mcp.server.fastmcp import FastMCP

from src.mcp_servers.phb_service import search_phb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("kob-phb")


@mcp.tool()
def get_context_from_phb(query: str) -> str:
    """Search the Player's Handbook (2024) for rules and lore; returns excerpts with Source lines (book + page)."""
    logger.info("PHB MCP tool: query=%r", query)
    return search_phb(query, k=3)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
