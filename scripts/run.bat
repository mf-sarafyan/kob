@echo off
REM Activate venv and run Streamlit app
setlocal

if not exist ".\.venv\Scripts\activate.bat" (
    echo Virtual env not found. Run scripts\setup.bat first.
    exit /b 1
)

call .\.venv\Scripts\activate.bat
set PYTHONPATH=%CD%
streamlit run src/app.py
