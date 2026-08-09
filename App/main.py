from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel

from App.services.upload_service import save_resume
from App.workflows.workflow import process_message
from App.services.parser_service import extract_text
from App.services.resume_analysis_service import analyze_resume
from App.services.job_matching_service import match_resume_with_job
from App.services.parser_service import extract_text

app = FastAPI(
    title="Job Search AI Agent",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str
    
@app.get("/")
def home():
    return {
        "message": "Job Search AI Agent is Running",
        "version": "1.0.0",
        "features": [
            "Resume Upload",
            "Resume RAG",
            "ATS Analysis",
            "Skills Analysis",
            "Job Matching"
        ]
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

@app.post("/analyze-resume")
def analyze_uploaded_resume(file: UploadFile = File(...)):

    result = save_resume(file)

    if not result.get("success"):
        return result

    file_path = result["filepath"]

    resume_text = extract_text(file_path)

    analysis = analyze_resume(resume_text)

    return {
        "success": True,
        "filename": result["filename"],
        "analysis": analysis
    }
@app.post("/match-job")
def match_job(
    job_description: str = Form(...),
    file: UploadFile = File(...)
):

    result = save_resume(file)

    if not result.get("success"):
        return result

    file_path = result["filepath"]

    resume_text = extract_text(file_path)

    analysis = match_resume_with_job(
        resume_text,
        job_description
    )

    return {
        "success": True,
        "filename": result["filename"],
        "job_match": analysis
    }    
