from app.rag.retriever import (
    retrieve_documents,
    detect_category
)


def main():

    print("=" * 60)
    print("CATEGORY-AWARE RETRIEVAL TEST")
    print("=" * 60)

    questions = [
        "What programming languages does Pasindu know?",
        "What are Pasindu's university qualifications?",
        "Tell me about the SLFloodWatch project.",
        "What certifications has Pasindu completed?"
    ]

    for question in questions:

        category = detect_category(question)

        print("\nQuestion:", question)
        print("Detected category:", category)
        print("-" * 60)

        results = retrieve_documents(
            question=question,
            k=3
        )

        for index, document in enumerate(results, start=1):

            print(f"\nResult {index}")
            print("Category:", document.metadata.get("category"))
            print("Source:", document.metadata.get("source"))
            print(document.page_content[:250])


if __name__ == "__main__":
    main()
