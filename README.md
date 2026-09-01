# Job Search AI Agent

AI-powered career assistant built using **FastAPI**, **React (Vite)**, **LangChain**, **FAISS Vector Database**, and **Google Gemini** for job search, resume analysis, and career guidance.

---

## 🚀 Quick Start (Local Run)

Double-click the [run_app.bat](run_app.bat) file in the root directory. It will start both:
- **FastAPI Backend** on `http://127.0.0.1:8000`
- **React Frontend** on `http://localhost:5173`

---

## 📂 Project Structure

- `backend/` - Core backend
  - `src/` - Backend source code
    - `agents/` - LLM agents (RAG, career guidance)
    - `database/` - FAISS vector database logic
    - `services/` - Services (parsing, embeddings, job matching, resume analysis)
    - `workflows/` - App workflows
    - `main.py` - FastAPI app initialization and routing
  - `tests/` - Unit and integration tests
- `shared/` - Shared resources
  - `Assets/` - Local storage (uploaded resumes, FAISS index files)
  - `data/` - Additional data files
- `job_env/` - Isolated python virtual environment
- `run_app.bat` - Unified double-click startup script

---

## 🌟 Core Features

1. **Resume Parser**: Extracts text from PDF and DOCX documents.
2. **ATS Scoring & Analysis**: Uses `gemini-3.6-flash` to evaluate resumes and calculate a score out of 100 with actionable strengths, weaknesses, and keyword suggestions.
3. **Semantic Job Matching**: Compares parsed resumes with any given job description to find missing/matching skills and score overall alignment.
4. **RAG Career Chatbot**: Uses a FAISS vector search index to perform similarity searches on your resume chunks, sending context to Gemini to answer questions truthfully without hallucination.

---

## 🌍 Deployment

The React frontend is set up for Firebase Hosting under project **`job-search-312e3`**:
- **Live URL**: `https://job-search-312e3.web.app`

---

## 🧪 Running Tests

You can run individual test modules from the project root using:
```powershell
job_env\Scripts\python.exe -m pytest backend/tests/test_parser
job_env\Scripts\python.exe -m pytest backend/tests/test_chunking
job_env\Scripts\python.exe -m pytest backend/tests/test_faiss
job_env\Scripts\python.exe -m pytest backend/tests/test_retrieval
```
