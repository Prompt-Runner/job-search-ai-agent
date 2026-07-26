from fastapi import FastAPI
from pydantic import BaseModel
from App.workflows.workflow import process_message

app = FastAPI(
    title="Job Search AI Agent",
    version="1.0.0",
    description="AI-powered Job Search Assistant"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Job Search AI Agent API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    return process_message(request.message)