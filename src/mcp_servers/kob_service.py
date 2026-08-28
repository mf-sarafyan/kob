"""
Shared campaign knowledge-base tools (graph + BM25) for the KOB MCP server.
Reuses LangChain tool implementations; returns strings (JSON for graph_search).
"""
from __future__ import annotations

import json
import logging
from functools import lru_cache
from typing import List, Optional

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def _kob_tools():
    from src.agents.tools import (
        SearchEntityTool,
        EntityDetailsTool,
        EntityConnectionsTool,
        RelatedEntitiesTool,
        create_search_tools,
    )
    from src.rag.index import create_rag_index
    from src.settings import CONTENT_DIR, INDEX_DIR

    content_dir = str(CONTENT_DIR.resolve())
    index_dir = str(INDEX_DIR.resolve())

    vector_store, graph_builder, _ = create_rag_index(content_dir, index_dir)
    vector_tool, graph_tool = create_search_tools(vector_store, graph_builder)
    logger.info("KOB MCP: RAG index and search tools ready (%s)", index_dir)
    return {
        "search_entity": SearchEntityTool(),
        "entity_details": EntityDetailsTool(),
        "entity_connections": EntityConnectionsTool(),
        "related_entities": RelatedEntitiesTool(),
        "vector_search": vector_tool,
        "graph_search": graph_tool,
    }


def kob_search_entity(query: str) -> str:
    return _kob_tools()["search_entity"]._run(query)


def kob_entity_details(query: str) -> str:
    return _kob_tools()["entity_details"]._run(query)


def kob_entity_connections(query: str) -> str:
    return _kob_tools()["entity_connections"]._run(query)


def kob_related_entities(query: str, max_depth: int = 2) -> str:
    return _kob_tools()["related_entities"]._run(query, max_depth)


def kob_vector_search(query: str, return_type: str = "entities") -> str:
    return _kob_tools()["vector_search"]._run(query, return_type)


def kob_graph_search(
    entity_name: str,
    max_depth: int = 2,
    relationship_types: Optional[str] = None,
) -> str:
    """
    Explore the campaign graph for an entity. Optional relationship_types: comma-separated names.
    """
    types_list: Optional[List[str]] = None
    if relationship_types and relationship_types.strip():
        types_list = [t.strip() for t in relationship_types.split(",") if t.strip()]
    raw = _kob_tools()["graph_search"]._run(
        entity_name, max_depth=max_depth, relationship_types=types_list
    )
    try:
        return json.dumps(raw, ensure_ascii=False, indent=2)
    except TypeError:
        return str(raw)
