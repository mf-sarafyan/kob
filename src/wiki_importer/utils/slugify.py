from __future__ import annotations
import re


def slugify(text: str) -> str:
    t = text.strip().lower()
    t = re.sub(r"[^\w\s-]", "", t)
    t = re.sub(r"[\s_-]+", "-", t)
    return t.strip("-") or "untitled"

