from fastapi import FastAPI
from pydantic import BaseModel

from App.workflows.workflow import process_message

app = FastAPI(
    title="Job Search AI Agent",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Job Search AI Agent is Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return process_message(request.message)