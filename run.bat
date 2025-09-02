@echo off
echo ========================================
echo    Healthcare Chatbot - Quick Start
echo ========================================
echo.
echo Choose your preferred interface:
echo.
echo 1. Flask Web App (Recommended)
echo 2. Streamlit App
echo 3. Install Dependencies
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting Flask application...
    python start_flask.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Streamlit application...
    python start_streamlit.py
) else if "%choice%"=="3" (
    echo.
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
    echo Dependencies installed! Please run this script again.
    pause
) else if "%choice%"=="4" (
    echo Goodbye!
    exit /b 0
) else (
    echo Invalid choice. Please run the script again.
    pause
)

pause
