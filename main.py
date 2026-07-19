from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

app = FastAPI(title="Job Search AI Agent")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Job Search AI Agent is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = model.generate_content(request.message)
    return {
        "user": request.message,
        "response": response.text
    }