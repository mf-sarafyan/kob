"""
Compose Note - Create markdown note from JSON structured data

Usage:
    python -m src.wiki_importer.compose_note <json_file> [--vault-root PATH]
    
Example:
    python -m src.wiki_importer.compose_note outputs/mind-flayer_20251216_200717.json
    
Output markdown files are saved to the vault directory based on note type.
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

from src.wiki_importer.configs.settings import default_settings
from src.wiki_importer.composer.composer import compose_note_from_json


def main():
    parser = argparse.ArgumentParser(
        description="Compose a markdown note from JSON structured data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  %(prog)s outputs/mind-flayer_20251216_200717.json --vault-root ./content
  
Output markdown files are saved to the vault directory based on note type.
        """
    )
    
    parser.add_argument(
        "json_file",
        help="Path to the JSON file in outputs/ folder"
    )
    
    parser.add_argument(
        "--vault-root",
        type=str,
        required=True,
        help="Root path of the Obsidian vault"
    )
    
    parser.add_argument(
        "--download-image",
        action="store_true",
        help="Download image if URL is available"
    )
    
    args = parser.parse_args()
    
    try:
        json_path = Path(args.json_file)
        print(f"Loading JSON: {json_path.name}")
        
        # Get settings
        settings = default_settings(args.vault_root)
        
        # Compose note
        output_path = compose_note_from_json(
            json_file=args.json_file,
            settings=settings,
            download_image=args.download_image,
        )
        
        print(f"\n✓ Created note: {output_path}")
    except KeyboardInterrupt:
        print("\n\nComposition cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nComposition failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

