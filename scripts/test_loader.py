
from app.rag.loader import load_knowledge_base


def main():
    documents = load_knowledge_base()

    print("\nKnowledge Base Loading Results")
    print("=" * 50)

    print(f"Total documents loaded: {len(documents)}")

    for index, document in enumerate(documents, start=1):
        print(f"\nDocument {index}")
        print(f"Source: {document.metadata.get('source')}")
        print(f"Content length: {len(document.page_content)} characters")
        print(f"Preview: {document.page_content[:150]}...")


if __name__ == "__main__":
    main()
