@echo off
cd /d "%~dp0"

REM Get git username
for /f %%u in ('git config user.name') do set username=%%u

REM Get date/time stamp
for /f "tokens=1-5 delims=/:. " %%d in ("%date% %time%") do (
    set datestamp=%%d-%%e-%%f_%%g-%%h
)

REM Create a unique branch name
set branch_name=update-%username%-%datestamp%

REM Create and switch to the branch
git checkout -b %branch_name%

REM Add and commit changes
git add .
git commit -m "Update by %username% at %datestamp%"
git push -u origin %branch_name%

echo.
echo ✅ Changes pushed to branch: %branch_name%
echo 🔗 Now go to GitHub and create a pull request from this branch!
pause
