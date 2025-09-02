# 🚀 Quick Start Guide - Healthcare Chatbot

## 📋 Prerequisites
- Python 3.8 or higher
- OpenAI API key
- pip (Python package installer)

## ⚡ Super Quick Start (Recommended)

### 1. Setup Environment
```bash
# Copy the environment template
cp .env.example .env

# Edit .env file and add your OpenAI API key
# OPENAI_API_KEY=your_actual_api_key_here
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application

#### Option A: Use the Quick Start Scripts
```bash
# Windows
run.bat

# Linux/Mac
chmod +x run.sh
./run.sh
```

#### Option B: Direct Commands
```bash
# Flask Web App (Recommended)
python start_flask.py

# OR Streamlit App
python start_streamlit.py
```

## 🌐 Access Your Application

### Flask Web App
- **URL**: http://localhost:5000
- **Features**: Modern web interface, mobile-friendly, real-time chat
- **API**: http://localhost:5000/chat

### Streamlit App
- **URL**: http://localhost:8501
- **Features**: Interactive dashboard, session management

## 🔧 Configuration

All configuration is managed through the `.env` file:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional (with defaults)
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=True
STREAMLIT_PORT=8501
LOG_LEVEL=INFO
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0.7
OPENAI_MAX_TOKENS=400
MAX_MESSAGE_LENGTH=1000
```

## 🛠️ Troubleshooting

### Common Issues

1. **"API key not configured" error**
   - Make sure you have a `.env` file with your OpenAI API key
   - Verify the key is valid and has sufficient credits

2. **"Module not found" errors**
   - Run `pip install -r requirements.txt`
   - Make sure you're in the correct directory

3. **Port already in use**
   - Change the port in your `.env` file
   - Or kill the process using the port

4. **Permission denied (Linux/Mac)**
   - Run `chmod +x run.sh` to make the script executable

### Getting Help
- Check the console output for detailed error messages
- Ensure all dependencies are installed correctly
- Verify your OpenAI API key is valid and active

## 📁 Project Structure
```
chatbot/
├── app.py              # Streamlit application
├── flask_app.py        # Flask web application
├── chatbot.py          # Core AI logic
├── config.py           # Configuration management
├── start_flask.py      # Flask startup script
├── start_streamlit.py  # Streamlit startup script
├── run.bat            # Windows quick start
├── run.sh             # Linux/Mac quick start
├── requirements.txt   # Python dependencies
├── .env.example      # Environment template
├── .env              # Your environment variables (create this)
└── templates/
    └── index.html    # Web interface
```

## 🎯 Features

- 🤖 **AI-Powered**: Uses OpenAI GPT-3.5 Turbo
- 🎨 **Modern UI**: Beautiful, responsive design
- 📱 **Mobile-Friendly**: Works on all devices
- ⚡ **Real-time**: Instant responses with typing indicators
- 🛡️ **Secure**: API keys in environment variables
- 🔧 **Configurable**: Easy to customize settings
- 📊 **Logging**: Comprehensive logging and error handling

## ⚠️ Important Notes

- This is for general health information only
- Always consult healthcare professionals for medical advice
- Never commit your `.env` file to version control
- The application includes proper error handling and validation

## 🚀 Ready to Go!

Your healthcare chatbot is now ready to use! Choose your preferred interface and start chatting with the AI assistant.
