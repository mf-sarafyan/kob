from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

NoteType = Literal["creature", "faction", "location", "character", "item", "entry"]


@dataclass(frozen=True)
class VaultPaths:
    vault_root: Path
    notes_by_type: dict[NoteType, Path]
    assets_by_type: dict[NoteType, Path]


@dataclass(frozen=True)
class ImportRules:
    required_frontmatter_by_type: dict[NoteType, list[str]]
    available_parameters_by_type: dict[NoteType, list[str]]
    default_tags: list[str]


@dataclass(frozen=True)
class Settings:
    paths: VaultPaths
    rules: ImportRules
    user_agent: str = "WikiImporter/0.1"


def default_settings(vault_root: str | Path) -> Settings:
    vr = Path(vault_root)

    notes_by_type: dict[NoteType, Path] = {
        "creature": vr / "wiki/creature",
        "faction":  vr / "wiki/faction",
        "location": vr / "wiki/location",
        "character": vr / "wiki/character",
        "item":     vr / "wiki/item",
        "entry":    vr / "wiki/entry",
    }

    assets_by_type: dict[NoteType, Path] = {
        "creature": vr / "assets/creatures",
        "faction":  vr / "assets/factions",
        "location": vr / "assets/locations",
        "character": vr / "assets/characters",
        "item":     vr / "assets/items",
        "entry":    vr / "assets/entry",
    }

    required = {
        "creature": ["title", "source", "source_url"],
        "faction":  ["title", "source", "source_url"],
        "location": ["title", "source", "source_url"],
        "character": ["title"],
        "item":     ["title", "source", "source_url"],
        "entry":    ["title", "source_url"],
    }

    available_parameters = {
        "character": ["origin", "class", "race", "known_locations", "factions", "alignment", "appears_in", "image"],
        "faction": ["parent", "location", "faction_type", "alignment", "leader", "appears_in"],
        "item": ["relates_to", "item_type", "item_rarity"],
        "location": ["location_type", "parent", "appears_in", "image"],
        "creature": ["creature_type", "size", "usual_alignment", "origin", "known_locations", "appears_in", "image"], 
        "entry": ["entry_type", "relates_to", "author"], 
    }

    return Settings(
        paths=VaultPaths(vr, notes_by_type, assets_by_type),
        rules=ImportRules(
            required_frontmatter_by_type=required,
            available_parameters_by_type=available_parameters,
            default_tags=["wiki-import"]
        ),
    )

