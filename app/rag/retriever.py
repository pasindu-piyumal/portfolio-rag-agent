
from functools import lru_cache

from app.rag.vector_store import get_vector_store


CATEGORY_KEYWORDS = {
    "technical_skills": [
        "skill", "skills", "programming", "language",
        "languages", "python", "java", "database",
        "framework", "technology", "technologies"
    ],

    "education": [
        "education", "university", "degree",
        "qualification", "qualifications",
        "academic", "cgpa", "gpa", "study"
    ],

    "projects": [
        "project", "projects", "slfloodwatch",
        "braintumerai", "moodlens",
        "student result", "inflation"
    ],

    "certifications": [
        "certification", "certifications",
        "certificate", "certificates",
        "coursera", "udemy"
    ],

    "experience": [
        "experience", "volunteer", "volunteering",
        "ieee", "extracurricular", "activities"
    ],

    "contact": [
        "contact", "email", "phone",
        "linkedin", "github", "portfolio link"
    ],

    "profile": [
        "about", "introduce", "introduction",
        "who is", "background", "summary"
    ]
}


@lru_cache(maxsize=1)
def get_cached_vector_store():
    """Load and reuse the ChromaDB vector store."""
    return get_vector_store()


def detect_category(question: str):
    question = question.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in question for keyword in keywords):
            return category

    return None


def retrieve_documents(question: str, k: int = 3):

    vector_store = get_cached_vector_store()

    category = detect_category(question)

    if category:
        results = vector_store.similarity_search(
            query=question,
            k=k,
            filter={"category": category}
        )
    else:
        results = vector_store.similarity_search(
            query=question,
            k=k
        )

    return results
