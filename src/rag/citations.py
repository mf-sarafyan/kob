"""
Human-readable source lines for RAG chunks (wiki paths, note titles, PDF pages).
"""
from __future__ import annotations

import os
from typing import Any, Dict, Mapping, Optional, Union

Meta = Union[Mapping[str, Any], Dict[str, Any]]


def _meta_str(meta: Meta, *keys: str) -> str:
    for k in keys:
        v = meta.get(k) if hasattr(meta, "get") else None
        if v is not None and str(v) not in ("", "unknown"):
            return str(v)
    return ""


def format_citation_line(
    metadata: Meta,
    *,
    include_full_path: bool = False,
    title_override: Optional[str] = None,
) -> str:
    """
    One-line citation for a chunk (for tool output and RAG context headers).

    :param metadata: LangChain Document.metadata or equivalent dict
    :param include_full_path: If True, append full filesystem path when available
    :param title_override: Short work title (e.g. PHB) instead of inferring from path
    """
    source = _meta_str(metadata, "source", "file_path")
    basename = os.path.basename(source) if source else ""
    title = title_override or (os.path.splitext(basename)[0] if basename else "") or "unknown"

    parent = _meta_str(metadata, "parent_entity")
    chunk_raw = metadata.get("chunk_id")
    if chunk_raw is None:
        chunk_raw = metadata.get("chunk_index")

    parts: list[str] = []
    if parent:
        parts.append(f"«{parent}»")
    chunk_part = ""
    if chunk_raw is not None and str(chunk_raw) not in ("", "unknown"):
        try:
            if int(chunk_raw) >= 0:
                chunk_part = f", chunk {chunk_raw}"
        except (TypeError, ValueError):
            pass

    page_raw = metadata.get("page")
    page_part = ""
    if page_raw is not None:
        try:
            page_part = f", p. {int(page_raw) + 1}"
        except (TypeError, ValueError):
            pass

    if title_override:
        parts.append(f"{title_override}{page_part}{chunk_part}")
    else:
        parts.append(f"`{title}`{chunk_part}{page_part}")

    line = " ".join(parts)
    if include_full_path and source and source != basename:
        line = f"{line} — {source}"
    return line


def format_sourced_text_block(
    page_content: str,
    metadata: Meta,
    *,
    max_chars: Optional[int] = 600,
    title_override: Optional[str] = None,
) -> str:
    """
    Citation header + body, for pasting into LLM context or tool results.
    """
    cite = format_citation_line(
        metadata, include_full_path=False, title_override=title_override
    )
    body = (page_content or "").strip()
    if max_chars is not None and len(body) > max_chars:
        body = body[: max_chars - 3].rstrip() + "..."
    return f"Source: {cite}\n\n{body}"
