@echo off
cd /d "%~dp0"
git checkout main
git pull


echo.
echo ✅ Vault updated with latest changes!
pause
