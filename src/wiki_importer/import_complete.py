"""
Complete Wiki Import - Extract, process, and compose in one go

Usage:
    python -m src.wiki_importer.import_complete <url> --note-type <type> --vault-root PATH
    
Example:
    python -m src.wiki_importer.import_complete https://forgottenrealms.fandom.com/wiki/Mind_flayer --note-type creature --vault-root ./content
    
This script combines all steps:
1. Extract wiki page content
2. Process with AI to extract structured data
3. Compose final markdown note
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

from src.wiki_importer.configs.settings import default_settings, NoteType
from src.wiki_importer.extractor.fandom import extract_fandom_page
from src.wiki_importer.agent.openai_agent import extract_json_structured_data
from src.wiki_importer.composer.composer import (
    compose_note_from_json,
    build_frontmatter_from_json,
    build_content_from_json,
    compose_markdown,
    validate_required,
    write_note,
    download_primary_image,
    find_image_url_in_txt_file,
)
from src.wiki_importer.utils.slugify import slugify
from src.wiki_importer.utils.files import ensure_dir


def import_and_compose(
    url: str,
    note_type: NoteType,
    vault_root: str | Path,
    source_name: str | None = None,
    download_image: bool = False,
    save_intermediates: bool = False,
) -> Path:
    """
    Complete import workflow: extract wiki page, process with AI, compose note.
    
    Args:
        url: URL of the wiki page to import
        note_type: Type of note (creature, faction, location, character, item, entry)
        vault_root: Root path of the Obsidian vault
        source_name: Optional source name (auto-detected from URL if not provided)
        download_image: Whether to download image if available
        save_intermediates: Whether to save intermediate .txt and .json files
    
    Returns:
        Path to the created markdown note
    """
    # Step 1: Extract wiki page
    print(f"Step 1: Extracting wiki page...")
    print(f"  URL: {url}")
    
    if source_name is None:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        if "fandom.com" in domain:
            subdomain = domain.split(".")[0]
            if subdomain and subdomain != "www":
                source_name = f"{subdomain.replace('-', ' ').title()} Wiki"
            else:
                source_name = "Fandom Wiki"
        else:
            source_name = domain.replace("www.", "").title()
    
    print(f"  Source: {source_name}")
    
    page = extract_fandom_page(url, user_agent="WikiImporter/0.1", source_name=source_name)
    print(f"  ✓ Extracted: {page.title}")
    
    # Optionally save intermediate .txt file
    txt_path = None
    if save_intermediates:
        outputs_dir = Path(__file__).parent / "outputs"
        ensure_dir(outputs_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{slugify(page.title)}_{timestamp}.txt"
        txt_path = outputs_dir / filename
        
        lines = [
            f"Title: {page.title}",
            f"Source URL: {page.source_url}",
            f"Source Name: {page.source_name}",
            "",
            "=" * 80,
            "",
        ]
        
        if page.image_candidates:
            lines.append(f"Image Candidates ({len(page.image_candidates)}):")
            for i, img in enumerate(page.image_candidates, 1):
                lines.append(f"  {i}. [{img.kind}] {img.url}")
            lines.append("")
        
        lines.extend([
            "=" * 80,
            "Content:",
            "=" * 80,
            "",
            page.raw_text,
            "",
            "=" * 80,
        ])
        
        txt_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"  ✓ Saved intermediate .txt: {txt_path}")
    
    # Step 2: Process with AI
    print(f"\nStep 2: Processing with AI agent...")
    print(f"  Note type: {note_type}")
    
    settings = default_settings(vault_root)
    available_params = settings.rules.available_parameters_by_type.get(note_type, [])
    
    print(f"  Calling LLM to extract structured data...")
    json_data = extract_json_structured_data(
        note_type=note_type,
        title=page.title,
        raw_text=page.raw_text,
        available_params=available_params,
    )
    
    # Add metadata
    json_data["source_url"] = page.source_url
    json_data["source_name"] = page.source_name
    json_data["extracted_at"] = datetime.now().isoformat()
    
    # Ensure 'type' field exists (agent may return 'note_type' for backwards compatibility)
    if "note_type" in json_data and "type" not in json_data:
        json_data["type"] = json_data.pop("note_type")
    
    # Optionally save intermediate .json file
    json_path = None
    if save_intermediates:
        if txt_path:
            json_path = txt_path.parent / f"{txt_path.stem}.json"
        else:
            outputs_dir = Path(__file__).parent / "outputs"
            ensure_dir(outputs_dir)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{slugify(page.title)}_{timestamp}.json"
            json_path = outputs_dir / filename
        
        json_path.write_text(
            json.dumps(json_data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        print(f"  ✓ Saved intermediate .json: {json_path}")
    
    # Step 3: Compose note
    print(f"\nStep 3: Composing markdown note...")
    
    # Build frontmatter
    frontmatter = build_frontmatter_from_json(json_data)
    
    # Handle image if present and download_image is True
    if download_image:
        # Try to get image from parameters
        image_url = json_data.get("parameters", {}).get("image")
        if not image_url and page.image_candidates:
            # Use first image candidate
            image_url = page.image_candidates[0].url
        
        if image_url:
            print(f"  Downloading image from: {image_url}")
            try:
                image_path = download_primary_image(
                    settings, note_type, page.title, image_url  # type: ignore
                )
                # Format as Obsidian link: [[image_path]]
                frontmatter["image"] = f"[[{image_path}]]"
                print(f"  ✓ Image saved: {image_path}")
            except Exception as e:
                print(f"  ⚠ Warning: Failed to download image: {e}")
    
    # Validate required fields
    validate_required(settings, note_type, frontmatter)  # type: ignore
    
    # Build content
    content = build_content_from_json(json_data)
    
    # Compose markdown
    markdown = compose_markdown(frontmatter, content)
    
    # Write note
    output_path = write_note(settings, note_type, page.title, markdown)  # type: ignore
    
    print(f"\n✓ Complete! Created note: {output_path}")
    
    return output_path


def get_default_vault_root() -> Path:
    """Get the default vault root path relative to project root."""
    # Get the project root (3 levels up from this file: src/wiki_importer/import_complete.py)
    # import_complete.py -> wiki_importer/ -> src/ -> kob/
    project_root = Path(__file__).parent.parent.parent
    return project_root / "content" / "1 Keepers' Compendium"


def main():
    default_vault = get_default_vault_root()
    
    parser = argparse.ArgumentParser(
        description="Complete wiki import: extract, process, and compose in one go",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Example:
  %(prog)s https://forgottenrealms.fandom.com/wiki/Mind_flayer --type creature
  
Default vault root: {default_vault}

This combines all steps:
1. Extract wiki page content
2. Process with AI to extract structured data
3. Compose final markdown note
        """
    )
    
    parser.add_argument(
        "url",
        help="URL of the wiki page to import"
    )
    
    parser.add_argument(
        "--type",
        required=True,
        choices=["creature", "faction", "location", "character", "item", "entry"],
        help="Type of note"
    )
    
    parser.add_argument(
        "--vault-root",
        type=str,
        default=str(default_vault),
        help=f"Root path of the Obsidian vault (default: {default_vault})"
    )
    
    parser.add_argument(
        "--source-name",
        type=str,
        default=None,
        help="Source name (auto-detected from URL if not provided)"
    )
    
    parser.add_argument(
        "--download-image",
        action="store_true",
        help="Download image if URL is available"
    )
    
    parser.add_argument(
        "--save-intermediates",
        action="store_true",
        help="Save intermediate .txt and .json files to outputs/ directory"
    )
    
    args = parser.parse_args()
    
    # Resolve vault root path
    vault_root = Path(args.vault_root).resolve()
    print(f"Using vault root: {vault_root}")
    
    try:
        import_and_compose(
            url=args.url,
            note_type=args.type,  # type: ignore
            vault_root=vault_root,
            source_name=args.source_name,
            download_image=args.download_image,
            save_intermediates=args.save_intermediates,
        )
    except KeyboardInterrupt:
        print("\n\nImport cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nImport failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

