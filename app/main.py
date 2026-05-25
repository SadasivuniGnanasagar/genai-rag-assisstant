from fastapi import FastAPI
from pydantic import BaseModel

# Services
from app.services.index_service import load_documents
from app.services.retrieval_service import retrieve_chunks
from app.services.llm_service import ask_llm
from app.services.memory_service import (
    get_history,
    save_message
)
from app.services.pdf_service import generate_pdf

# Prompt Builder
from app.prompts.prompt_builder import build_prompt


# Initialize FastAPI
app = FastAPI()


# Load documents into vector DB at startup
load_documents()


# Request Model
class ChatRequest(BaseModel):
    sessionId: str
    message: str


# Health Check API
@app.get("/")
def health():
    return {
        "status": "working"
    }


# Chat API
@app.post("/api/chat")
def chat(request: ChatRequest):

    try:

        # Step 1: Get conversation history
        history = get_history(request.sessionId)

        # Step 2: Retrieve relevant chunks
        retrieved = retrieve_chunks(request.message)

        # If no chunks found
        if not retrieved:
            return {
                "reply": "I could not find enough information in the knowledge base."
            }

        # Step 3: Build context
        context = "\n".join(
            [chunk["text"] for chunk in retrieved]
        )

        # Step 4: Build prompt
        prompt = build_prompt(
            context=context,
            history=history,
            question=request.message
        )

        # Step 5: Generate LLM response
        response = ask_llm(prompt)

        # Step 6: Save chat memory
        save_message(
            request.sessionId,
            "user",
            request.message
        )

        save_message(
            request.sessionId,
            "assistant",
            response
        )

        # Step 7: Generate PDF report
        pdf_path = generate_pdf(
            request.message,
            response
        )

        # Step 8: Return response
        return {
            "reply": response,
            "retrievedChunks": len(retrieved),
            "pdfReport": pdf_path
        }

    except Exception as e:

        return {
            "error": str(e)
        }