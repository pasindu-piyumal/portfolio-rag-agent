from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import DirectoryLoader, TextLoader

BASE_DIR = Path(__file__).resolve().parents[2]
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"


CATEGORY_MAP = {
    "01_personal_profile.md": "profile",
    "02_education.md": "education",
    "03_technical_skills.md": "technical_skills",
    "04_projects.md": "projects",
    "05_experience_and_activities.md": "experience",
    "06_certifications.md": "certifications",
    "07_contact_information.md": "contact"
}


def load_knowledge_base() -> list[Document]:

    if not KNOWLEDGE_BASE_DIR.exists():
        raise FileNotFoundError(
            f"Knowledge base directory not found: {KNOWLEDGE_BASE_DIR}"
        )

    loader = DirectoryLoader(
        str(KNOWLEDGE_BASE_DIR),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True
    )

    documents = loader.load()

    for document in documents:

        filename = Path(document.metadata["source"]).name

        category = CATEGORY_MAP.get(filename, "general")

        document.metadata["category"] = category

    if not documents:
        raise ValueError("No Markdown documents found.")

    return documents
