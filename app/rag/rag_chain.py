from app.llm.gemini import get_gemini_model
from app.rag.retriever import retrieve_documents

def generate_answer(question: str) -> dict:
    """
    Generate an answer using retrieved portfolio information.
    """

    # Retrieve relevant documents
    documents = retrieve_documents(
        question=question,
        k=3
    )

    # Handle questions with no retrieved context
    if not documents:
        return {
            "question": question,
            "answer": "I couldn't find relevant information in Pasindu's portfolio.",
            "sources": []
        }

    # Combine retrieved content
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # Initialize Gemini
    model = get_gemini_model()

        # Create RAG prompt
    prompt = f"""
You are the AI portfolio assistant for Pasindu Piyumal.

Answer the user's question using ONLY the provided portfolio context.

INFORMATION RULES:
1. Use the provided context as your source of information.
2. Do not invent qualifications, skills, projects, or experience.
3. If the answer is not available in the context, clearly say so.
4. Give clear, professional, and helpful answers.
5. Do not mention internal retrieval processes.

RESPONSE FORMATTING RULES:
1. Use clear headings and structured paragraphs.
2. Use Unicode bold characters for headings instead of Markdown bold.
3. Do not use ** or __ for bold formatting.
4. Use bullet points when listing multiple items.
5. Use numbered lists for step-by-step instructions.
6. Keep responses professional, friendly, and easy to read.
7. Use code blocks for programming examples when relevant.
8. Highlight important information using Unicode bold text.
9. Preserve the original meaning of the retrieved information.
10. Avoid unnecessarily long responses.

UNICODE BOLD EXAMPLE:
Instead of:
**Programming Languages**

Use:
𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗶𝗻𝗴 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀

IMPORTANT:
- Apply Unicode bold characters only to headings and important labels.
- Keep normal descriptions and technical terms readable.
- Do not convert entire paragraphs into Unicode bold.
- Never use Markdown bold syntax.

Portfolio Context:
{context}

User Question:
{question}

Answer:
"""

    # Generate response
    response = model.invoke(prompt)

    # Collect source documents
    sources = list(set(
        document.metadata.get("source", "Unknown")
        for document in documents
    ))

    return {
        "question": question,
        "answer": (
            response.content
            if isinstance(response.content, str)
            else "".join(
                block.get("text", "")
                for block in response.content
                if isinstance(block, dict)
            )
        ),
        "sources": sources
    }
