from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from App.services.upload_service import save_resume
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


@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):
    return save_resume(file)


@app.post("/chat")
def chat(request: ChatRequest):
    return process_message(request.message)