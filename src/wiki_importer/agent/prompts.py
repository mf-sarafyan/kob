from __future__ import annotations
from src.wiki_importer.configs.settings import NoteType


def build_prompt(entry_type: NoteType, title: str, raw_text: str) -> str:
    # Keep this short; you can refine later.
    return f"""

You are converting and summarizing a wiki article into an Obsidian note for a D&D campaign.

Entry type: {entry_type}
Title: {title}

Rules:
- Do NOT invent lore.
- Remove trivia, citations, and wiki meta.
- Keep game-relevant lore.
- Output Markdown ONLY for the body (no YAML).

Body structure:

## Overview

## Lore

## Spelljammer Notes

## DM Notes

Article text:

{raw_text}

""".strip()

