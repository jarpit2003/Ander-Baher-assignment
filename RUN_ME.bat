@echo off
title Andar-Baher Support API - Server
color 0A
echo ========================================
echo   Andar-Baher Support API Server
echo ========================================
echo.
echo Starting server...
echo.
echo Once started, open your browser and go to:
echo   http://127.0.0.1:8000/docs
echo.
echo Press CTRL+C to stop the server
echo.
echo ========================================
echo.
cd /d "%~dp0"
call .\.venv\Scripts\activate.bat
python -m uvicorn api:app --reload


