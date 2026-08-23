from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form
)

from fastapi.middleware.cors import CORSMiddleware

import os
import shutil
import tempfile

from App.services.upload_service import save_resume
from App.services.parser_service import extract_text
from App.services.resume_analysis_service import analyze_resume
from App.services.job_matching_service import match_job
from App.services.gemini_service import generate_response


app = FastAPI(
    title="Job Search AI Agent",
    version="2.0.0"
)


# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=False,

    allow_methods=["*"],

    allow_headers=["*"],
)


# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():

    return {
        "success": True,
        "message": "Job Search AI Agent is Running",
        "version": "2.0.0"
    }


# =====================================================
# HEALTH
# =====================================================

@app.get("/health")
def health():

    return {
        "status": "Healthy",
        "backend": "FastAPI",
        "ai": "Gemini"
    }


# =====================================================
# UPLOAD RESUME
# =====================================================

@app.post("/upload-resume")
async def upload_resume(
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

    temp_path = None

    try:

        extension = os.path.splitext(
            file.filename
        )[1].lower()

        if extension not in [
            ".pdf",
            ".docx",
            ".txt"
        ]:

            return {
                "success": False,
                "error": "Only PDF, DOCX, and TXT files are supported."
            }

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        ) as temp_file:

            temp_path = temp_file.name

            content = await file.read()

            temp_file.write(content)

        resume_text = extract_text(
            temp_path
        )

        if not resume_text.strip():

            return {
                "success": False,
                "error": "Could not extract text from resume."
            }

        result = analyze_resume(
            resume_text
        )

        return {
            "success": True,
            "filename": file.filename,
            "analysis": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    finally:

        if temp_path and os.path.exists(
            temp_path
        ):

            os.remove(temp_path)


# =====================================================
# JOB MATCHING
# =====================================================

@app.post("/match-job")
async def match_job_api(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    temp_path = None

    try:

        extension = os.path.splitext(
            file.filename
        )[1].lower()

        if extension not in [
            ".pdf",
            ".docx",
            ".txt"
        ]:

            return {
                "success": False,
                "error": "Only PDF, DOCX, and TXT files are supported."
            }

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        ) as temp_file:

            temp_path = temp_file.name

            content = await file.read()

            temp_file.write(content)

        resume_text = extract_text(
            temp_path
        )

        if not resume_text.strip():

            return {
                "success": False,
                "error": "Could not extract resume text."
            }

        if not job_description.strip():

            return {
                "success": False,
                "error": "Job description is required."
            }

        result = match_job(
            resume_text,
            job_description
        )

        return {
            "success": True,
            "filename": file.filename,
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    finally:

        if temp_path and os.path.exists(
            temp_path
        ):

            os.remove(temp_path)


# =====================================================
# AI ASSISTANT
# =====================================================

@app.post("/chat")
async def chat(
    message: str = Form(...),
    file: UploadFile | None = File(None)
):

    temp_path = None

    try:

        resume_context = ""

        if file:

            extension = os.path.splitext(
                file.filename
            )[1].lower()

            if extension not in [
                ".pdf",
                ".docx",
                ".txt"
            ]:

                return {
                    "success": False,
                    "error": "Only PDF, DOCX, and TXT files are supported."
                }

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=extension
            ) as temp_file:

                temp_path = temp_file.name

                content = await file.read()

                temp_file.write(content)

            resume_context = extract_text(
                temp_path
            )

        prompt = f"""
You are a helpful AI career assistant.

Answer the user's question clearly.

USER QUESTION:
{message}

RESUME CONTEXT:
{resume_context}

Rules:

- If resume context is provided, use it.
- Do not invent information about the candidate.
- If the answer is not available, say so.
- Give practical career advice.
"""

        response = generate_response(
            prompt
        )

        return {
            "success": True,
            "message": message,
            "response": response
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    finally:

        if temp_path and os.path.exists(
            temp_path
        ):

            os.remove(temp_path)