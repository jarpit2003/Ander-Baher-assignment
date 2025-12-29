@echo off
echo Starting Andar-Baher Support API Server...
echo.
echo Server will be available at: http://127.0.0.1:8000
echo Swagger UI will be available at: http://127.0.0.1:8000/docs
echo.
echo Press CTRL+C to stop the server
echo.
cd /d "%~dp0"
.\.venv\Scripts\python.exe -m uvicorn api:app --reload


