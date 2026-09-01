@echo off
echo ========================================================
echo Starting Job Search AI Agent Application...
echo ========================================================

:: Start the FastAPI Backend
echo [1/2] Starting FastAPI Backend on port 8000...
start "Job Search Backend" cmd /k "job_env\Scripts\python.exe -m uvicorn backend.src.main:app --port 8000"

:: Start the Vite React Frontend
echo [2/2] Starting React Frontend on port 5173...
start "Job Search Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"

echo --------------------------------------------------------
echo Both services are starting in separate windows.
echo - Backend API: http://127.0.0.1:8000
echo - Frontend UI: http://localhost:5173
echo --------------------------------------------------------
pause
