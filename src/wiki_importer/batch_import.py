"""
Batch Wiki Import - Process multiple wiki pages in sequence

Usage:
    python -m src.wiki_importer.batch_import <batch_file> [--vault-root PATH]
    
Example batch file (batch.txt or batch.json):
    # JSON format:
    [
        ["https://spelljammer.fandom.com/wiki/Airslug", "creature"],
        ["https://spelljammer.fandom.com/wiki/Bral", "location"],
        ["https://forgottenrealms.fandom.com/wiki/Mind_flayer", "creature"]
    ]
    
    # Or text format (one per line: url|type):
    https://spelljammer.fandom.com/wiki/Airslug|creature
    https://spelljammer.fandom.com/wiki/Bral|location
    https://forgottenrealms.fandom.com/wiki/Mind_flayer|creature
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Any

from src.wiki_importer.configs.settings import NoteType
from src.wiki_importer.import_complete import import_and_compose, get_default_vault_root


def load_batch_file(batch_file: str | Path) -> list[tuple[str, NoteType]]:
    """
    Load batch file containing URLs and types.
    
    Supports:
    - JSON format: [["url", "type"], ...]
    - Text format: url|type (one per line)
    
    Args:
        batch_file: Path to batch file
    
    Returns:
        List of (url, type) tuples
    """
    batch_path = Path(batch_file)
    if not batch_path.exists():
        raise FileNotFoundError(f"Batch file not found: {batch_path}")
    
    content = batch_path.read_text(encoding="utf-8").strip()
    
    # Try JSON first
    if content.startswith("[") or content.startswith("{"):
        try:
            data = json.loads(content)
            if isinstance(data, list):
                return [(item[0], item[1]) for item in data if len(item) >= 2]  # type: ignore
        except json.JSONDecodeError:
            pass
    
    # Fall back to text format (url|type)
    items = []
    for line in content.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        if "|" in line:
            parts = line.split("|", 1)
            if len(parts) == 2:
                url = parts[0].strip()
                note_type = parts[1].strip()
                items.append((url, note_type))  # type: ignore
    
    if not items:
        raise ValueError(f"No valid entries found in batch file: {batch_path}")
    
    return items


def batch_import(
    batch_file: str | Path,
    vault_root: str | Path,
    download_image: bool = False,
    save_intermediates: bool = False,
    continue_on_error: bool = True,
) -> dict[str, Any]:
    """
    Process multiple wiki pages from a batch file.
    
    Args:
        batch_file: Path to batch file with URLs and types
        vault_root: Root path of the Obsidian vault
        download_image: Whether to download images
        save_intermediates: Whether to save intermediate files
        continue_on_error: Whether to continue processing if one fails
    
    Returns:
        Dictionary with success/failure counts and details
    """
    batch_path = Path(batch_file)
    print(f"Loading batch file: {batch_path.name}")
    
    items = load_batch_file(batch_path)
    print(f"Found {len(items)} items to process\n")
    
    results = {
        "total": len(items),
        "successful": [],
        "failed": [],
    }
    
    for i, (url, note_type) in enumerate(items, 1):
        print(f"{'=' * 80}")
        print(f"Processing {i}/{len(items)}: {url}")
        print(f"Type: {note_type}")
        print(f"{'=' * 80}\n")
        
        try:
            output_path = import_and_compose(
                url=url,
                note_type=note_type,  # type: ignore
                vault_root=vault_root,
                download_image=download_image,
                save_intermediates=save_intermediates,
            )
            
            results["successful"].append({
                "url": url,
                "type": note_type,
                "output": str(output_path),
            })
            
            print(f"\n✓ Successfully processed: {url}\n")
            
        except Exception as e:
            error_msg = str(e)
            results["failed"].append({
                "url": url,
                "type": note_type,
                "error": error_msg,
            })
            
            print(f"\n✗ Failed to process: {url}")
            print(f"  Error: {error_msg}\n")
            
            if not continue_on_error:
                print("Stopping batch processing due to error.")
                break
    
    # Print summary
    print(f"\n{'=' * 80}")
    print("BATCH PROCESSING SUMMARY")
    print(f"{'=' * 80}")
    print(f"Total: {results['total']}")
    print(f"Successful: {len(results['successful'])}")
    print(f"Failed: {len(results['failed'])}")
    
    if results["failed"]:
        print(f"\nFailed items:")
        for item in results["failed"]:
            print(f"  - {item['url']} ({item['type']}): {item['error']}")
    
    # Save results to file
    results_file = batch_path.parent / f"{batch_path.stem}_results.json"
    results_file.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    print(f"\nResults saved to: {results_file}")
    
    return results


def main():
    default_vault = get_default_vault_root()
    
    parser = argparse.ArgumentParser(
        description="Batch process multiple wiki pages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Batch file formats:

JSON format:
  [
    ["https://spelljammer.fandom.com/wiki/Airslug", "creature"],
    ["https://spelljammer.fandom.com/wiki/Bral", "location"]
  ]

Text format (url|type):
  https://spelljammer.fandom.com/wiki/Airslug|creature
  https://spelljammer.fandom.com/wiki/Bral|location
  # Lines starting with # are ignored
        """
    )
    
    parser.add_argument(
        "batch_file",
        help="Path to batch file (JSON or text format)"
    )
    
    parser.add_argument(
        "--vault-root",
        type=str,
        default=str(default_vault),
        help=f"Root path of the Obsidian vault (default: {default_vault})"
    )
    
    parser.add_argument(
        "--download-image",
        action="store_true",
        help="Download images if available"
    )
    
    parser.add_argument(
        "--save-intermediates",
        action="store_true",
        help="Save intermediate .txt and .json files"
    )
    
    parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop processing if an error occurs (default: continue)"
    )
    
    args = parser.parse_args()
    
    vault_root = Path(args.vault_root).resolve()
    print(f"Using vault root: {vault_root}\n")
    
    try:
        batch_import(
            batch_file=args.batch_file,
            vault_root=vault_root,
            download_image=args.download_image,
            save_intermediates=args.save_intermediates,
            continue_on_error=not args.stop_on_error,
        )
    except KeyboardInterrupt:
        print("\n\nBatch processing cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nBatch processing failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

