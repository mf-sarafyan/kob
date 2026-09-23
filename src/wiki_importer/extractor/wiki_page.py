from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class ImageCandidate:
    url: str
    kind: str  # "infobox" | "og" | "content" | etc.


@dataclass(frozen=True)
class ExtractedPage:
    title: str
    source_name: str
    source_url: str
    raw_text: str
    image_candidates: list[ImageCandidate]

