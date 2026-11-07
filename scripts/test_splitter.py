from app.rag.loader import load_knowledge_base
from app.rag.splitter import split_documents


def main():

    documents = load_knowledge_base()

    chunks = split_documents(documents)

    print("\nDocument Splitting Results")
    print("=" * 50)

    print(f"Original documents: {len(documents)}")
    print(f"Total chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):

        print(f"\nChunk {index}")
        print(f"Source: {chunk.metadata.get('source')}")
        print(f"Length: {len(chunk.page_content)} characters")
        print(f"Content:\n{chunk.page_content[:250]}")


if __name__ == "__main__":
    main()
