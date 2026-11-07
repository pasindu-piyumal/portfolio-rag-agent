import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
from app.rag.vector_store import create_vector_store

load_dotenv()


def main():

    print("=" * 60)
    print("REBUILDING CHROMADB WITH CATEGORY METADATA")
    print("=" * 60)

    persist_directory = Path(
        os.getenv("CHROMA_PERSIST_DIRECTORY", "chroma_db")
    )

    # Remove the old vector database
    if persist_directory.exists():

        print("\nRemoving old ChromaDB database...")

        shutil.rmtree(persist_directory)

    print("\nCreating updated vector database...")

    vector_store = create_vector_store()

    print("\nVector database rebuilt successfully!")

    # Verify stored documents
    stored_data = vector_store.get()

    print("\nStored Chunks:", len(stored_data["ids"]))

    print("\nStored Categories:")
    
    categories = set(
        metadata.get("category", "unknown")
        for metadata in stored_data["metadatas"]
    )

    for category in sorted(categories):
        print("-", category)

    print("\nChromaDB metadata verification completed!")


if __name__ == "__main__":
    main()
