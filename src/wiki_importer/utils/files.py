from __future__ import annotations
from pathlib import Path


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_utf8(p: Path, content: str) -> None:
    ensure_dir(p.parent)
    p.write_text(content, encoding="utf-8")

