"""
Configuration management for Healthcare Chatbot
This module handles all configuration settings and environment variables.
"""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Healthcare Chatbot application."""
    
    # OpenAI Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", "400"))
    OPENAI_TIMEOUT: int = int(os.getenv("OPENAI_TIMEOUT", "30"))
    
    # Flask Configuration
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG: bool = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    FLASK_HOST: str = os.getenv("FLASK_HOST", "0.0.0.0")
    FLASK_PORT: int = int(os.getenv("FLASK_PORT", "5000"))
    
    # Streamlit Configuration
    STREAMLIT_PORT: int = int(os.getenv("STREAMLIT_PORT", "8501"))
    
    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Security Configuration
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production")
    
    # Application Configuration
    APP_NAME: str = "Healthcare Chatbot"
    APP_VERSION: str = "1.0.0"
    MAX_MESSAGE_LENGTH: int = int(os.getenv("MAX_MESSAGE_LENGTH", "1000"))
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that all required configuration is present."""
        required_vars = ["OPENAI_API_KEY"]
        missing_vars = []
        
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
            return False
        
        return True
    
    @classmethod
    def get_openai_config(cls) -> dict:
        """Get OpenAI configuration as a dictionary."""
        return {
            "api_key": cls.OPENAI_API_KEY,
            "model": cls.OPENAI_MODEL,
            "temperature": cls.OPENAI_TEMPERATURE,
            "max_tokens": cls.OPENAI_MAX_TOKENS,
            "timeout": cls.OPENAI_TIMEOUT
        }
    
    @classmethod
    def get_flask_config(cls) -> dict:
        """Get Flask configuration as a dictionary."""
        return {
            "host": cls.FLASK_HOST,
            "port": cls.FLASK_PORT,
            "debug": cls.FLASK_DEBUG,
            "env": cls.FLASK_ENV
        }
    
    @classmethod
    def print_config(cls):
        """Print current configuration (excluding sensitive data)."""
        print("🔧 Current Configuration:")
        print(f"  App Name: {cls.APP_NAME} v{cls.APP_VERSION}")
        print(f"  OpenAI Model: {cls.OPENAI_MODEL}")
        print(f"  OpenAI Temperature: {cls.OPENAI_TEMPERATURE}")
        print(f"  OpenAI Max Tokens: {cls.OPENAI_MAX_TOKENS}")
        print(f"  Flask Host: {cls.FLASK_HOST}")
        print(f"  Flask Port: {cls.FLASK_PORT}")
        print(f"  Flask Debug: {cls.FLASK_DEBUG}")
        print(f"  Streamlit Port: {cls.STREAMLIT_PORT}")
        print(f"  Log Level: {cls.LOG_LEVEL}")
        print(f"  Max Message Length: {cls.MAX_MESSAGE_LENGTH}")
        print(f"  OpenAI API Key: {'✅ Set' if cls.OPENAI_API_KEY else '❌ Not Set'}")

# Create a global config instance
config = Config()
