@echo off
echo ============================================================
echo   PII Redaction Tool - Privacy Shield
echo ============================================================
echo.
echo [*] Starting server at http://localhost:5000
echo.
echo [*] Opening browser in 3 seconds...
echo.
cd /d "%~dp0"
start "" "http://localhost:5000"
python app.py
pause
