from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from App.services.upload_service import save_resume
from App.workflows.workflow import process_message


app = FastAPI(
    title="Job Search AI Agent",
    version="1.0.0"
)


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):
    return save_resume(file)