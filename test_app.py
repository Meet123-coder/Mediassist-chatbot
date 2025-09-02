#!/usr/bin/env python3
"""
Test script for Healthcare Chatbot
This script tests the basic functionality of the chatbot.
"""

import os
import sys
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported."""
    print("🧪 Testing imports...")
    
    try:
        import flask
        print("✅ Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        import flask_cors
        print("✅ Flask-CORS imported successfully")
    except ImportError as e:
        print(f"❌ Flask-CORS import failed: {e}")
        return False
    
    try:
        import openai
        print("✅ OpenAI imported successfully")
    except ImportError as e:
        print(f"❌ OpenAI import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
        return False
    
    return True

def test_config():
    """Test configuration loading."""
    print("\n🔧 Testing configuration...")
    
    try:
        from config import config
        print("✅ Config module imported successfully")
        
        if config.OPENAI_API_KEY:
            print("✅ OpenAI API key is configured")
        else:
            print("⚠️  OpenAI API key is not configured")
            print("   Please add your API key to the .env file")
        
        return True
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False

def test_chatbot():
    """Test chatbot functionality."""
    print("\n🤖 Testing chatbot...")
    
    try:
        from chatbot import get_healthcare_response
        print("✅ Chatbot module imported successfully")
        
        # Test with a simple message
        test_message = "Hello, how are you?"
        print(f"📝 Testing with message: '{test_message}'")
        
        response = get_healthcare_response(test_message)
        print(f"✅ Bot response: {response[:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Chatbot test failed: {e}")
        return False

def test_flask_app():
    """Test Flask app creation."""
    print("\n🌐 Testing Flask app...")
    
    try:
        from flask_app import app
        print("✅ Flask app imported successfully")
        
        # Test app creation
        with app.test_client() as client:
            response = client.get('/health')
            if response.status_code == 200:
                print("✅ Health endpoint working")
            else:
                print(f"⚠️  Health endpoint returned status {response.status_code}")
        
        return True
    except Exception as e:
        print(f"❌ Flask app test failed: {e}")
        return False

def main():
    """Main test function."""
    print("=" * 60)
    print("🏥 Healthcare Chatbot - Test Suite")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_config,
        test_chatbot,
        test_flask_app
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your chatbot is ready to use.")
        print("\n🚀 To start the application:")
        print("   - Flask: python start_flask.py")
        print("   - Streamlit: python start_streamlit.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
