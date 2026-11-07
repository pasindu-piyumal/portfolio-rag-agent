import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from app.rag.embeddings import get_embedding_model
from app.rag.loader import load_knowledge_base
from app.rag.splitter import split_documents

load_dotenv()


def create_vector_store():
    """
    Load, split, embed, and store knowledge-base documents in ChromaDB.
    """

    persist_directory = os.getenv(
        "CHROMA_PERSIST_DIRECTORY",
        "chroma_db"
    )

    embedding_model = get_embedding_model()

    documents = load_knowledge_base()
    chunks = split_documents(documents)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name="portfolio_knowledge",
        persist_directory=persist_directory
    )

    return vector_store


def get_vector_store():
    """
    Load an existing ChromaDB collection.
    """

    persist_directory = os.getenv(
        "CHROMA_PERSIST_DIRECTORY",
        "chroma_db"
    )

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        collection_name="portfolio_knowledge",
        embedding_function=embedding_model,
        persist_directory=persist_directory
    )

    return vector_store
