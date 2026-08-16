from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from App.services.upload_service import save_resume
from App.services.resume_analysis_service import analyze_resume

from App.workflows.workflow import process_message


app = FastAPI(
    title="Job Search AI Agent",
    version="1.0.0"
)


# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================================
# REQUEST MODEL
# =====================================================

class ChatRequest(BaseModel):
    message: str


# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():
    return {
        "message": "Job Search AI Agent is Running"
    }


# =====================================================
# HEALTH
# =====================================================

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


# =====================================================
# CHAT
# =====================================================

@app.post("/chat")
def chat(request: ChatRequest):

    return process_message(
        request.message
    )


# =====================================================
# RESUME UPLOAD
# =====================================================

@app.post("/upload-resume")
def upload_resume(
    file: UploadFile = File(...)
):

    return save_resume(file)


# =====================================================
# RESUME ANALYSIS
# =====================================================

@app.post("/analyze-resume")
async def analyze_resume_api(
    file: UploadFile = File(...)
):

    try:

        # Read uploaded file
        file_content = await file.read()

        # Analyze resume
        result = analyze_resume(
            file_content,
            file.filename
        )

        return result

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }