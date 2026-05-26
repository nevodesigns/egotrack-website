@echo off
REM EgoTrack Waitlist Server - Quick Start for Windows

echo ======================================
echo EgoTrack Waitlist Server Starting...
echo ======================================
echo.

REM Check if .env file exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please create a .env file with your Gmail credentials.
    echo Refer to SETUP_GUIDE.md for instructions.
    pause
    exit /b 1
)

REM Check if Flask is installed
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo Starting Flask server...
echo.
echo Email notifications will be sent to: nwokoloebube21@gmail.com
echo Website will be available at: http://localhost:5000
echo.
echo Press CTRL+C to stop the server
echo.

python app.py
pause
