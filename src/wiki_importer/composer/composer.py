from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
import hashlib
import json
from typing import Any

from src.wiki_importer.configs.settings import Settings, NoteType
from src.wiki_importer.utils.slugify import slugify
from src.wiki_importer.utils.files import ensure_dir, write_utf8
from src.wiki_importer.utils.yaml_frontmatter import wrap_frontmatter
from src.wiki_importer.utils.http import get_bytes


def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _guess_ext(url: str) -> str:
    ext = Path(urlparse(url).path).suffix.lower()
    if ext in [".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"]:
        return ext
    return ".png"


def download_primary_image(
    settings: Settings,
    entry_type: NoteType,
    title: str,
    image_url: str,
) -> str:
    assets_dir = settings.paths.assets_by_type.get(entry_type, settings.paths.assets_by_type["entry"])
    ensure_dir(assets_dir)

    ext = _guess_ext(image_url)
    base = slugify(title)
    target = assets_dir / f"{base}{ext}"

    data = get_bytes(image_url, user_agent=settings.user_agent)
    h = _sha256(data)

    if target.exists() and _sha256(target.read_bytes()) != h:
        target = assets_dir / f"{base}-{h[:10]}{ext}"

    target.write_bytes(data)

    # Return vault-relative path
    return str(target.relative_to(settings.paths.vault_root)).replace("\\", "/")


def validate_required(settings: Settings, entry_type: NoteType, fm: dict) -> None:
    required = settings.rules.required_frontmatter_by_type.get(entry_type, ["title"])
    missing = [k for k in required if not fm.get(k)]
    if missing:
        raise ValueError(f"Missing required frontmatter for '{entry_type}': {missing}")


def compose_markdown(frontmatter: dict, content: str) -> str:
    return f"{wrap_frontmatter(frontmatter)}\n\n{content.strip()}\n"


def write_note(
    settings: Settings,
    entry_type: NoteType,
    title: str,
    markdown: str,
) -> Path:
    note_dir = settings.paths.notes_by_type.get(entry_type, settings.paths.notes_by_type["entry"])
    ensure_dir(note_dir)
    
    base_filename = slugify(title)
    out = note_dir / f"{base_filename}.md"
    
    # If file already exists, append "- wiki import" to avoid overwriting
    if out.exists():
        out = note_dir / f"{base_filename} - wiki import.md"
    
    write_utf8(out, markdown)
    return out


def load_json_file(json_path: Path) -> dict[str, Any]:
    """Load and parse JSON file."""
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    
    content = json_path.read_text(encoding="utf-8")
    return json.loads(content)


def capitalize_title(title: str) -> str:
    """Capitalize title properly (title case)."""
    # Simple title case - capitalize first letter of each word
    return title.title()


def build_frontmatter_from_json(json_data: dict[str, Any]) -> dict[str, Any]:
    """
    Build frontmatter dictionary from JSON data.
    
    Args:
        json_data: Dictionary loaded from JSON file
    
    Returns:
        Frontmatter dictionary ready for YAML
    """
    title = capitalize_title(json_data["title"])
    frontmatter = {
        "title": title,
        "type": json_data.get("note_type") or json_data.get("type"),  # Support both for backwards compatibility
        "source": json_data.get("source_name", "Unknown"),
        "source_url": json_data.get("source_url", ""),
    }
    
    # Add all parameters from the JSON
    parameters = json_data.get("parameters", {})
    for key, value in parameters.items():
        # Skip null values
        if value is not None:
            frontmatter[key] = value
    
    # Add tags
    frontmatter["tags"] = ["wiki-import"]
    
    return frontmatter


def build_content_from_json(json_data: dict[str, Any]) -> str:
    """
    Build markdown content from JSON data.
    
    Args:
        json_data: Dictionary loaded from JSON file
    
    Returns:
        Markdown content string
    """
    summary = json_data.get("summary", "")
    parameters = json_data.get("parameters", {})
    
    lines = []
    
    # Add summary if available
    if summary:
        lines.append("## Overview\n")
        lines.append(summary)
        lines.append("")
    
    # Add parameter sections if they contain meaningful data
    if parameters:
        # Group related parameters
        location_params = []
        if parameters.get("known_locations"):
            location_params.extend(parameters["known_locations"])
        if parameters.get("location"):
            location_params.append(parameters["location"])
        
        if location_params:
            lines.append("## Locations\n")
            for loc in location_params:
                lines.append(f"- {loc}")
            lines.append("")
        
        # Add other notable parameters as a details section
        notable_params = {}
        for key, value in parameters.items():
            if key not in ["known_locations", "location", "image"] and value:
                if isinstance(value, list) and len(value) > 0:
                    notable_params[key] = value
                elif not isinstance(value, list):
                    notable_params[key] = value
        
        if notable_params:
            lines.append("## Details\n")
            for key, value in notable_params.items():
                key_display = key.replace("_", " ").title()
                if isinstance(value, list):
                    lines.append(f"**{key_display}**: {', '.join(str(v) for v in value)}")
                else:
                    lines.append(f"**{key_display}**: {value}")
            lines.append("")
    
    return "\n".join(lines).strip()


def find_image_url_in_txt_file(txt_path: Path) -> str | None:
    """
    Try to find image URL in the original .txt file.
    
    Args:
        txt_path: Path to the .txt file
    
    Returns:
        Image URL if found, None otherwise
    """
    if not txt_path.exists():
        return None
    
    content = txt_path.read_text(encoding="utf-8")
    for line in content.split("\n"):
        if line.startswith("  1. [infobox]") or line.startswith("  1. [og]"):
            # Extract URL from line like "  1. [infobox] https://..."
            parts = line.split("] ", 1)
            if len(parts) == 2:
                return parts[1].strip()
    return None


def compose_note_from_json(
    json_file: str | Path,
    settings: Settings,
    download_image: bool = False,
) -> Path:
    """
    Compose a markdown note from a JSON file.
    
    Args:
        json_file: Path to the JSON file
        settings: Settings object with vault paths and rules
        download_image: Whether to download image if URL is available
    
    Returns:
        Path to the created markdown file
    """
    json_path = Path(json_file)
    
    # Load JSON data
    json_data = load_json_file(json_path)
    
    # Support both 'type' and 'note_type' for backwards compatibility
    note_type = json_data.get("type") or json_data.get("note_type")
    title = json_data["title"]
    
    # Build frontmatter
    frontmatter = build_frontmatter_from_json(json_data)
    
    # Handle image if present and download_image is True
    if download_image:
        # Try to get image from parameters
        image_url = json_data.get("parameters", {}).get("image")
        if not image_url:
            # Try to get from original .txt file if it exists
            txt_path = json_path.parent / f"{json_path.stem}.txt"
            image_url = find_image_url_in_txt_file(txt_path)
        
        if image_url:
            try:
                image_path = download_primary_image(
                    settings, note_type, title, image_url  # type: ignore
                )
                # Format as Obsidian link: [[image_path]]
                frontmatter["image"] = f"[[{image_path}]]"
            except Exception:
                # Silently fail - image download is optional
                pass
    
    # Validate required fields
    validate_required(settings, note_type, frontmatter)  # type: ignore
    
    # Build content
    content = build_content_from_json(json_data)
    
    # Compose markdown
    markdown = compose_markdown(frontmatter, content)
    
    # Write note
    output_path = write_note(settings, note_type, title, markdown)  # type: ignore
    
    return output_path

