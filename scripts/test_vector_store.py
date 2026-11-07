from app.rag.vector_store import create_vector_store

def main():

    print("=" * 60)
    print("PORTFOLIO RAG AGENT - CHROMADB TEST")
    print("=" * 60)

    try:

        print("\nCreating vector database...")

        vector_store = create_vector_store()

        print("\nVector database created successfully!")

        query = "What programming languages does Pasindu know?"

        print("\nSearching knowledge base...")
        print("Question:", query)

        results = vector_store.similarity_search(
            query,
            k=3
        )

        print("\nRetrieved Documents:")
        print("-" * 60)

        for index, document in enumerate(results, start=1):

            print(f"\nResult {index}")
            print("Source:", document.metadata.get("source"))
            print("Content:")
            print(document.page_content[:300])

        print("\nChromaDB test completed successfully!")

    except Exception as error:

        print("\nChromaDB test failed!")
        print("Error:", error)


if __name__ == "__main__":
    main()
