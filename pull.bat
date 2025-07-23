@echo off
cd /d "%~dp0"
git pull origin main
git checkout main

echo.
echo ✅ Vault updated with latest changes!
pause
