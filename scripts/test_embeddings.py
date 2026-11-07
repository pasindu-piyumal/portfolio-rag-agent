from app.rag.embeddings import get_embedding_model

def main():

    print("=" * 60)
    print("PORTFOLIO RAG AGENT - EMBEDDING MODEL TEST")
    print("=" * 60)

    try:

        embedding_model = get_embedding_model()

        print("\nEmbedding model initialized successfully!")

        text = "Pasindu is a Data Science undergraduate."

        print("\nGenerating embedding...")

        vector = embedding_model.embed_query(text)

        print("\nEmbedding generated successfully!")
        print("Vector dimensions:", len(vector))
        print("First 10 values:", vector[:10])

    except Exception as error:

        print("\nEmbedding model test failed!")
        print("Error:", error)


if __name__ == "__main__":
    main()
