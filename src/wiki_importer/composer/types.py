from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from src.wiki_importer.configs.settings import NoteType


@dataclass(frozen=True)
class ComposedNote:
    path: Path
    frontmatter: dict[str, Any]
    content: str
    markdown: str
    image_path: str | None

