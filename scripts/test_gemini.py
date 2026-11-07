from app.llm.gemini import get_gemini_model

def main():
    print("=" * 60)
    print("PORTFOLIO RAG AGENT - GEMINI CONNECTION TEST")
    print("=" * 60)

    try:
        model = get_gemini_model()

        print("\nSending test question to Gemini...")

        response = model.invoke(
            "Introduce yourself as an AI assistant "
            "for a Data Science undergraduate's portfolio."
        )

        print("\nGemini Response:")
        print(response.content)

        print("\nGemini API connection successful!")

    except Exception as error:

        print("\nGemini API connection failed!")
        print("Error:", error)


if __name__ == "__main__":
    main()
