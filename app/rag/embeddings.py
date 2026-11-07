
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


def get_embedding_model():
    """
    Initialize Gemini embeddings through Google's API.
    Embeddings are generated remotely instead of loading
    a local Hugging Face model.
    """

    model_name = os.getenv(
        "GEMINI_EMBEDDING_MODEL",
        "gemini-embedding-001"
    )

    embedding_model = GoogleGenerativeAIEmbeddings(
        model=model_name,
        output_dimensionality=768
    )

    return embedding_model
