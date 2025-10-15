@echo off
REM Create venv, install deps, and pull Ollama models
setlocal enabledelayedexpansion

python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Install Python 3.10+ and re-run.
    exit /b 1
)

python -m venv .venv
call .\.venv\Scripts\activate.bat

python -m pip install --upgrade pip
pip install -r requirements.txt

ollama --version >nul 2>&1
if errorlevel 1 (
    echo Ollama not found. Install from https://ollama.com and ensure 'ollama' is in PATH.
    exit /b 1
)

echo Pulling models (this may take a while)...
ollama pull llama3.1
ollama pull nomic-embed-text

echo Setup complete.
