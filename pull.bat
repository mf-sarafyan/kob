@echo off
cd /d "%~dp0"
git pull origin main

echo.
echo ✅ Vault updated with latest changes!
pause
