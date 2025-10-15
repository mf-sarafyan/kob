#!/usr/bin/env python3
"""
Detailed debugging script for content loading
"""
import sys
import os
from pathlib import Path

# Add src to path
sys.path.append('src')

from src.settings import CONTENT_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from src.rag.load import load_and_chunk

def main():
    print("=== CONTENT LOADING DEBUG ===")
    
    # Verify content directory
    print(f"Content Directory: {CONTENT_DIR}")
    print(f"Directory Exists: {CONTENT_DIR.exists()}")
    
    if not CONTENT_DIR.exists():
        print("ERROR: Content directory does not exist!")
        return
    
    # List all files in the directory
    print("\n=== ALL FILES IN CONTENT DIRECTORY ===")
    for root, dirs, files in os.walk(CONTENT_DIR):
        level = root.replace(str(CONTENT_DIR), '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{Path(root).name}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
    
    # Attempt to load and chunk content
    print("\n=== LOADING AND CHUNKING ===")
    try:
        chunks = load_and_chunk(CONTENT_DIR, CHUNK_SIZE, CHUNK_OVERLAP)
        print(f"\nTotal chunks created: {len(chunks)}")
        
        if chunks:
            print("\n=== FIRST CHUNK DETAILS ===")
            first_chunk = chunks[0]
            print(f"Source: {first_chunk.metadata.get('source', 'Unknown')}")
            print(f"Content Preview: {first_chunk.page_content[:500]}...")
        
    except Exception as e:
        print(f"ERROR during loading: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
