from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def _loader_for(path: Path):
    # Only process text files (markdown, txt, etc.) and PDFs
    try:
        if path.suffix.lower() == ".pdf":
            print(f"Loading PDF: {path}")
            return PyPDFLoader(str(path))
        elif path.suffix.lower() in [".md", ".txt", ".rst"]:
            print(f"Loading text file: {path}")
            # Try multiple encodings
            encodings = ['utf-8', 'latin-1', 'utf-16']
            for encoding in encodings:
                try:
                    loader = TextLoader(str(path), encoding=encoding)
                    # Test if the document can be loaded
                    loader.load()
                    return loader
                except Exception as e:
                    print(f"Failed to load {path} with {encoding} encoding: {e}")
            
            print(f"Could not load {path} with any encoding")
            return None
        else:
            # Skip other file types
            return None
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None


def load_and_chunk(content_dir: Path, chunk_size: int, chunk_overlap: int):
    print(f"Loading from directory: {content_dir}")
    print(f"Absolute path: {content_dir.resolve()}")
    
    # First, let's see what files we can find
    all_files = list(content_dir.rglob("*"))
    text_files = [f for f in all_files if f.is_file() and f.suffix.lower() in ['.md', '.txt', '.rst', '.pdf']]
    
    print(f"Found {len(text_files)} text files:")
    for f in text_files:
        print(f"  {f.relative_to(content_dir)} (size: {f.stat().st_size} bytes, suffix: {f.suffix})")
    
    if not text_files:
        print("No text files found! Check your content directory.")
        print("Directory contents:")
        for item in content_dir.iterdir():
            print(f"  {item} ({'directory' if item.is_dir() else 'file'})")
        return []
    
    # Manually create a list of file paths to load
    file_paths = [str(f) for f in text_files]
    
    # Detailed logging of file paths
    print("\n=== File Paths to Load ===")
    for path in file_paths:
        print(f"  {path}")
    
    # Create loaders manually for each file
    docs = []
    for path in file_paths:
        try:
            loader = _loader_for(Path(path))
            if loader:
                file_docs = loader.load()
                print(f"Loaded {len(file_docs)} documents from {path}")
                docs.extend(file_docs)
            else:
                print(f"Skipped loading {path}")
        except Exception as e:
            print(f"Error loading {path}: {e}")
    
    # Filter out any None results (from skipped files)
    docs = [doc for doc in docs if doc is not None]
    
    print(f"\nLoaded {len(docs)} total documents")
    
    # Print details about loaded documents
    for i, doc in enumerate(docs[:5], 1):
        print(f"Document {i}:")
        print(f"  Source: {doc.metadata.get('source', 'Unknown')}")
        print(f"  Content preview: {doc.page_content[:200]}...")
    
    if not docs:
        print("No documents were loaded! Check the file paths and permissions.")
        return []
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True,
    )
    
    try:
        chunks = splitter.split_documents(docs)
    except Exception as e:
        print(f"Error during document splitting: {e}")
        import traceback
        traceback.print_exc()
        return []
    
    print(f"Created {len(chunks)} chunks")
    
    # Print details about first few chunks
    for i, chunk in enumerate(chunks[:5], 1):
        print(f"Chunk {i}:")
        print(f"  Source: {chunk.metadata.get('source', 'Unknown')}")
        print(f"  Content preview: {chunk.page_content[:200]}...")
    
    return chunks


