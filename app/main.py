from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="Portfolio RAG Agent API",
    description="AI-powered portfolio assistant using Gemini and RAG.",
    version="1.0.0"
)


# CORS configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API routes
app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)


@app.get("/")
def home():
    return {
        "message": "Portfolio RAG Agent API is running!"
    }