import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()


def get_embedding_model():
    """
    Initialize and return the local Hugging Face embedding model.
    """

    model_name = os.getenv(
        "HF_EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    device = os.getenv(
        "HF_EMBEDDING_DEVICE",
        "cpu"
    )

    embedding_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={
            "device": device
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    return embedding_model
