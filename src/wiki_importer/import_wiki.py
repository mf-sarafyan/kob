"""
Simple Wiki Page Extractor - Extract wiki page and save to .txt file

Usage:
    python -m src.wiki_importer.import_wiki <url>
    
Example:
    python -m src.wiki_importer.import_wiki https://forgottenrealms.fandom.com/wiki/Mind_flayer
    
Output files are saved to: src/wiki_importer/outputs/
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from datetime import datetime

from src.wiki_importer.extractor.fandom import extract_fandom_page
from src.wiki_importer.utils.slugify import slugify
from src.wiki_importer.utils.files import ensure_dir


def print_wiki_page(url: str, user_agent: str = "WikiImporter/0.1", source_name: str | None = None):
    """
    Extract a wiki page's contents and save to a temporary .txt file.
    
    Args:
        url: URL of the wiki page to extract
        user_agent: User agent string for HTTP requests
        source_name: Optional source name (defaults to "Fandom Wiki")
    
    Returns:
        Path to the saved output file
    """
    if source_name is None:
        source_name = "Fandom Wiki"
    
    print(f"Extracting: {url}")
    print(f"Source: {source_name}")
    
    try:
        page = extract_fandom_page(url, user_agent=user_agent, source_name=source_name)
        
        # Create outputs directory
        outputs_dir = Path(__file__).parent / "outputs"
        ensure_dir(outputs_dir)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{slugify(page.title)}_{timestamp}.txt"
        output_path = outputs_dir / filename
        
        # Build output content
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
        
        # Write to file
        output_path.write_text("\n".join(lines), encoding="utf-8")
        
        print(f"\n✓ Saved to: {output_path}")
        print(f"  Title: {page.title}")
        if page.image_candidates:
            print(f"  Found {len(page.image_candidates)} image candidate(s)")
        
        return output_path
        
    except Exception as e:
        print(f"\n✗ Error extracting page: {e}", file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Extract a wiki page and save to .txt file in outputs/",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  %(prog)s https://forgottenrealms.fandom.com/wiki/Mind_flayer
  
Output files are saved to: src/wiki_importer/outputs/
        """
    )
    
    parser.add_argument(
        "url",
        help="URL of the wiki page to extract"
    )
    
    parser.add_argument(
        "--source-name",
        type=str,
        default=None,
        help="Source name (defaults to 'Fandom Wiki')"
    )
    
    args = parser.parse_args()
    
    try:
        print_wiki_page(
            url=args.url,
            user_agent="WikiImporter/0.1",
            source_name=args.source_name,
        )
    except KeyboardInterrupt:
        print("\n\nExtraction cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nExtraction failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

