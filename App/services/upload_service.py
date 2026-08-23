import os
import shutil
from fastapi import UploadFile

UPLOAD_FOLDER = "Assets/resumes"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_resume(file: UploadFile):

    allowed_extensions = [".pdf", ".docx", ".txt"]

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in allowed_extensions:
        return {
            "success": False,
            "message": "Only PDF, DOCX, and TXT files are allowed."
        }

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "success": True,
        "filename": file.filename,
        "filepath": filepath
    }