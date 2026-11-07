from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.rag.rag_chain import generate_answer

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = generate_answer(request.question)
        return ChatResponse(
            question=result["question"],
            answer=result["answer"],
            sources=result["sources"]
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )