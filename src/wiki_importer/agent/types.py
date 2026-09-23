from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from src.wiki_importer.configs.settings import NoteType


@dataclass(frozen=True)
class AgentInput:
    entry_type: NoteType
    title: str
    source: str
    source_url: str
    raw_text: str


@dataclass(frozen=True)
class AgentOutput:
    entry_type: NoteType
    frontmatter: dict[str, Any]
    content: str

