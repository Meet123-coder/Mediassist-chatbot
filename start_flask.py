#!/usr/bin/env python3
"""
Startup script for Flask Healthcare Chatbot
This script provides an easy way to start the Flask application with proper configuration.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_requirements():
    """Check if all required packages are installed."""
    try:
        import flask
        import openai
        import flask_cors
        from dotenv import load_dotenv
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists and has required variables."""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found")
        print("Please copy .env.example to .env and add your OpenAI API key")
        return False
    
    # Load and check environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY not found in .env file")
        print("Please add your OpenAI API key to the .env file")
        return False
    
    print("✅ Environment configuration is valid")
    return True

def main():
    """Main startup function."""
    print("🏥 Healthcare Chatbot - Flask Application")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check environment
    if not check_env_file():
        sys.exit(1)
    
    print("\n🚀 Starting Flask application...")
    print("📱 Frontend will be available at: http://localhost:5000")
    print("🔧 API endpoint: http://localhost:5000/chat")
    print("💚 Health check: http://localhost:5000/health")
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Start Flask app
        subprocess.run([sys.executable, "flask_app.py"], check=True)
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting Flask app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
