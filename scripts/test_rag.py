from app.rag.rag_chain import generate_answer

def main():

    print("=" * 60)
    print("PORTFOLIO RAG AGENT - GEMINI RAG TEST")
    print("=" * 60)

    questions = [
        "What programming languages does Pasindu know?",
        "What are Pasindu's university qualifications?",
        "Tell me about the SLFloodWatch project.",
        "What certifications has Pasindu completed?"
    ]

    for question in questions:

        print("\nQuestion:", question)
        print("-" * 60)

        try:

            result = generate_answer(question)

            print("\nAI Answer:")
            print(result["answer"])

            print("\nSources:")

            for source in result["sources"]:
                print("-", source)

        except Exception as error:

            print("\nError:", error)


if __name__ == "__main__":
    main()
