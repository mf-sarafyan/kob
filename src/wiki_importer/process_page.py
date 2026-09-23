"""
Process Wiki Page - Extract structured data from pre-ingested .txt files

Usage:
    python -m src.wiki_importer.process_page <input_file> --note-type <type>
    
Example:
    python -m src.wiki_importer.process_page outputs/mind-flayer_20251216_200717.txt --note-type creature
    
Output JSON files are saved to: src/wiki_importer/outputs/
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

from src.wiki_importer.configs.settings import default_settings, NoteType
from src.wiki_importer.agent.openai_agent import extract_json_structured_data


def parse_output_file(file_path: Path) -> dict[str, str]:
    """
    Parse a .txt output file and extract metadata and content.
    
    Returns:
        Dictionary with keys: title, source_url, source_name, raw_text
    """
    content = file_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    # Extract metadata from header
    title = ""
    source_url = ""
    source_name = ""
    
    content_start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith("Title: "):
            title = line.replace("Title: ", "").strip()
        elif line.startswith("Source URL: "):
            source_url = line.replace("Source URL: ", "").strip()
        elif line.startswith("Source Name: "):
            source_name = line.replace("Source Name: ", "").strip()
        elif line.startswith("Content:") and "=" * 80 in lines[i-1]:
            content_start_idx = i + 2  # Skip the separator line
            break
    
    # Extract raw text content (everything after "Content:" section)
    raw_text = "\n".join(lines[content_start_idx:]).strip()
    # Remove trailing separator if present
    if raw_text.endswith("=" * 80):
        raw_text = raw_text[:-80].strip()
    
    return {
        "title": title,
        "source_url": source_url,
        "source_name": source_name,
        "raw_text": raw_text,
    }


def process_page(
    input_file: str | Path,
    note_type: NoteType,
    vault_root: str | Path | None = None,
) -> Path:
    """
    Process a pre-ingested .txt file with the agent and output structured JSON.
    
    Args:
        input_file: Path to the .txt file in outputs/ folder
        note_type: Type of note (creature, faction, location, character, item, entry)
        vault_root: Optional vault root for settings (uses temp path if not provided)
    
    Returns:
        Path to the created JSON file
    """
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    print(f"Processing: {input_path.name}")
    
    # Parse the input file
    parsed = parse_output_file(input_path)
    print(f"  Title: {parsed['title']}")
    print(f"  Source: {parsed['source_name']}")
    
    # Get settings to access available parameters
    if vault_root is None:
        # Use a temp path just to get settings structure
        vault_root = Path("/tmp")
    settings = default_settings(vault_root)
    available_params = settings.rules.available_parameters_by_type.get(note_type, [])
    
    # Call LLM agent to extract structured data
    print("  Calling LLM agent to extract structured data...")
    try:
        json_data = extract_json_structured_data(
            note_type=note_type,
            title=parsed["title"],
            raw_text=parsed["raw_text"],
            available_params=available_params,
        )
    except json.JSONDecodeError as e:
        print(f"  ✗ Error: LLM did not return valid JSON: {e}", file=sys.stderr)
        # Save the raw response for debugging (if we can get it)
        debug_path = input_path.parent / f"{input_path.stem}_debug.txt"
        debug_path.write_text(str(e), encoding="utf-8")
        print(f"  Error details saved to: {debug_path}", file=sys.stderr)
        raise
    
    # Add metadata
    json_data["source_url"] = parsed["source_url"]
    json_data["source_name"] = parsed["source_name"]
    json_data["extracted_at"] = datetime.now().isoformat()
    
    # Save JSON file
    outputs_dir = input_path.parent
    json_filename = f"{input_path.stem}.json"
    json_path = outputs_dir / json_filename
    
    json_path.write_text(json.dumps(json_data, indent=2, ensure_ascii=False), encoding="utf-8")
    
    print(f"  ✓ Saved JSON to: {json_path}")
    
    return json_path


def main():
    parser = argparse.ArgumentParser(
        description="Process a pre-ingested .txt file and extract structured JSON",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  %(prog)s outputs/mind-flayer_20251216_200717.txt --note-type creature
  
Output JSON files are saved to: src/wiki_importer/outputs/
        """
    )
    
    parser.add_argument(
        "input_file",
        help="Path to the .txt file in outputs/ folder"
    )
    
    parser.add_argument(
        "--note-type",
        required=True,
        choices=["creature", "faction", "location", "character", "item", "entry"],
        help="Type of note"
    )
    
    parser.add_argument(
        "--vault-root",
        type=str,
        default=None,
        help="Optional vault root path (uses temp path if not provided)"
    )
    
    args = parser.parse_args()
    
    try:
        process_page(
            input_file=args.input_file,
            note_type=args.note_type,  # type: ignore
            vault_root=args.vault_root,
        )
    except KeyboardInterrupt:
        print("\n\nProcessing cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nProcessing failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

