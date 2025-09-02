#!/bin/bash

echo "========================================"
echo "   Healthcare Chatbot - Quick Start"
echo "========================================"
echo ""
echo "Choose your preferred interface:"
echo ""
echo "1. Flask Web App (Recommended)"
echo "2. Streamlit App"
echo "3. Install Dependencies"
echo "4. Exit"
echo ""
read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "Starting Flask application..."
        python3 start_flask.py
        ;;
    2)
        echo ""
        echo "Starting Streamlit application..."
        python3 start_streamlit.py
        ;;
    3)
        echo ""
        echo "Installing dependencies..."
        pip3 install -r requirements.txt
        echo ""
        echo "Dependencies installed! Please run this script again."
        ;;
    4)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        ;;
esac
