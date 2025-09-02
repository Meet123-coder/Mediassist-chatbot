#!/usr/bin/env python3
"""
Setup script for Healthcare Chatbot
This script helps you set up the environment and run the application.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_banner():
    """Print the application banner."""
    print("=" * 60)
    print("🏥 Healthcare Chatbot - Setup & Configuration")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required dependencies."""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True, text=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        print(f"   Error output: {e.stderr}")
        return False

def setup_env_file():
    """Set up the .env file."""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if not env_example.exists():
        print("❌ .env.example file not found")
        return False
    
    # Copy .env.example to .env
    shutil.copy(env_example, env_file)
    print("✅ Created .env file from template")
    
    # Get OpenAI API key from user
    print("\n🔑 OpenAI API Key Setup")
    print("You need an OpenAI API key to use this chatbot.")
    print("Get your API key from: https://platform.openai.com/api-keys")
    
    api_key = input("\nEnter your OpenAI API key (or press Enter to skip): ").strip()
    
    if api_key:
        # Update the .env file with the API key
        with open(env_file, 'r') as f:
            content = f.read()
        
        content = content.replace('your_openai_api_key_here', api_key)
        
        with open(env_file, 'w') as f:
            f.write(content)
        
        print("✅ API key saved to .env file")
    else:
        print("⚠️  You can add your API key later by editing the .env file")
    
    return True

def test_configuration():
    """Test the configuration."""
    print("\n🧪 Testing configuration...")
    try:
        from config import config
        if config.validate_config():
            print("✅ Configuration is valid")
            return True
        else:
            print("❌ Configuration validation failed")
            return False
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def show_next_steps():
    """Show next steps to the user."""
    print("\n🎉 Setup Complete!")
    print("\n📋 Next Steps:")
    print("1. If you haven't added your OpenAI API key yet, edit the .env file")
    print("2. Run the application using one of these methods:")
    print()
    print("   🚀 Quick Start:")
    print("   - Windows: run.bat")
    print("   - Linux/Mac: ./run.sh")
    print()
    print("   🔧 Direct Commands:")
    print("   - Flask App: python start_flask.py")
    print("   - Streamlit App: python start_streamlit.py")
    print()
    print("   🌐 Access URLs:")
    print("   - Flask: http://localhost:5000")
    print("   - Streamlit: http://localhost:8501")
    print()
    print("📖 For more details, see QUICK_START.md")

def main():
    """Main setup function."""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed during dependency installation")
        sys.exit(1)
    
    # Setup environment file
    if not setup_env_file():
        print("\n❌ Setup failed during environment setup")
        sys.exit(1)
    
    # Test configuration
    if not test_configuration():
        print("\n⚠️  Configuration test failed, but setup can continue")
        print("   Make sure to add your OpenAI API key to the .env file")
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    main()
