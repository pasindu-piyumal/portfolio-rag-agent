from app.rag.loader import load_knowledge_base

def main():

    documents = load_knowledge_base()

    print("\nDOCUMENT CATEGORY TEST")
    print("=" * 50)

    for document in documents:

        print(
            f"{document.metadata.get('category'):20} "
            f"| {document.metadata.get('source')}"
        )


if __name__ == "__main__":
    main()
