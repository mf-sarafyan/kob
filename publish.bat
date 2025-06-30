@echo off
cd /d "%~dp0"  REM This makes sure we run from the script's folder

REM Get the current date and time in a safe format
for /f "tokens=1-5 delims=/:. " %%d in ("%date% %time%") do (
    set datestamp=%%d-%%e-%%f_%%g-%%h
)

REM Add and commit everything
git add .
git commit -m "Auto-publish: %datestamp%"
git push

echo.
echo -------------------------------
echo ✔️  Pushed at %datestamp%
echo -------------------------------
pause