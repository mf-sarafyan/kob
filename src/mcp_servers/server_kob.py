"""
MCP server: KEEPERS campaign vault (wiki notes, knowledge graph, BM25 chunk search).

Run from repository root::

    python -m src.mcp_servers.server_kob

Cursor: command ``python``, args ``["-m", "src.mcp_servers.server_kob"]``, cwd = repo root.
"""
from __future__ import annotations

import logging
from typing import Optional

from mcp.server.fastmcp import FastMCP

from src.mcp_servers import kob_service as kob

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("kob-campaign")


@mcp.tool()
def search_entity(query: str) -> str:
    """Search the knowledge graph for entities by name or alias."""
    return kob.kob_search_entity(query)


@mcp.tool()
def entity_details(query: str) -> str:
    """Full note content and attributes for one entity; includes source file paths when available."""
    return kob.kob_entity_details(query)


@mcp.tool()
def entity_connections(query: str) -> str:
    """Incoming and outgoing relationships for an entity."""
    return kob.kob_entity_connections(query)


@mcp.tool()
def related_entities(query: str, max_depth: int = 2) -> str:
    """Multi-hop related entities from a starting entity name."""
    return kob.kob_related_entities(query, max_depth)


@mcp.tool()
def vector_search(query: str, return_type: str = "entities") -> str:
    """BM25 search over vault chunks. return_type: 'entities' (default) or 'documents'."""
    return kob.kob_vector_search(query, return_type)


@mcp.tool()
def graph_search(
    entity_name: str,
    max_depth: int = 2,
    relationship_types: Optional[str] = None,
) -> str:
    """Deep graph exploration for one entity. Optional relationship_types: comma-separated edge type names. Returns JSON."""
    return kob.kob_graph_search(entity_name, max_depth, relationship_types)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
