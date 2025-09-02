# 🏥 MediAssist - AI Healthcare Chatbot

**"Your AI-powered healthcare companion, guiding you toward better health every day."**

A modern, responsive healthcare chatbot built with Flask and OpenAI GPT-3.5 Turbo. This application provides a user-friendly interface for asking general health questions and receiving AI-powered responses.

## ✨ Features

- 🤖 **AI-Powered Responses**: Uses OpenAI GPT-3.5 Turbo for intelligent healthcare assistance
- 🎨 **Modern UI**: Beautiful, responsive design with gradient backgrounds and smooth animations
- 📱 **Mobile-Friendly**: Fully responsive design that works on all devices
- ⚡ **Real-time Chat**: Instant responses with typing indicators
- 🛡️ **Error Handling**: Comprehensive error handling and user feedback
- 🔒 **Secure**: API keys stored in environment variables
- 🏥 **Healthcare Focused**: Specialized prompts for medical information
- 🗑️ **Chat Management**: Clear chat functionality with confirmation
- ⌨️ **Keyboard Shortcuts**: Quick access with Ctrl+L to clear chat
- 🚀 **Standalone Mode**: Works offline with demo responses

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip (Python package installer)

## 🚀 Quick Start

### Option 1: Standalone Version (No Setup Required)
1. **Download** `standalone_chatbot.html`
2. **Double-click** to open in your browser
3. **Start chatting** - Works immediately with demo responses!

### Option 2: Full AI Version (Requires Setup)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mediassist-chatbot.git
   cd mediassist-chatbot
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

5. **Run the application**
   ```bash
   # Automated setup
   python setup.py
   
   # Or manual start
   python start_flask.py
   ```

## Usage

### Option 1: Flask Web Application (Recommended)

1. **Start the Flask server**
   ```bash
   python flask_app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:5000`
   - Start chatting with the AI healthcare assistant

### Option 2: Streamlit Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - Streamlit will automatically open the app in your default browser
   - Usually at `http://localhost:8501`

## API Endpoints

### Flask Application

- `GET /` - Main chat interface
- `POST /chat` - Send message and receive AI response
- `GET /health` - Health check endpoint

### Chat API Usage

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the symptoms of a common cold?"}'
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Customization

You can modify the following in `chatbot.py`:
- Model version (currently GPT-3.5 Turbo)
- Temperature (controls randomness)
- Max tokens (response length)
- System prompt (AI behavior)

## 📁 Project Structure

```
mediassist-chatbot/
├── 🚀 standalone_chatbot.html    # Standalone version (works offline)
├── 🌐 flask_app.py              # Flask web application
├── 📱 app.py                    # Streamlit application
├── 🤖 chatbot.py                # Core AI logic and OpenAI integration
├── ⚙️ config.py                 # Configuration management
├── 🛠️ setup.py                  # Automated setup script
├── 🚀 start_flask.py            # Flask startup script
├── 📱 start_streamlit.py        # Streamlit startup script
├── 🧪 test_app.py               # Test suite
├── 📦 requirements.txt          # Python dependencies
├── 🔧 .env.example             # Environment variables template
├── 🚫 .gitignore               # Git ignore file
├── 📖 README.md                # This file
├── 📋 QUICK_START.md           # Quick start guide
├── 🖥️ run.bat                  # Windows quick start
├── 🐧 run.sh                   # Linux/Mac quick start
└── 📁 templates/
    └── index.html              # Web interface template
```

## Security Notes

- ⚠️ **Never commit your `.env` file** - it contains sensitive API keys
- 🔒 API keys are loaded from environment variables, not hardcoded
- 🛡️ Input validation and error handling prevent common vulnerabilities

## Troubleshooting

### Common Issues

1. **"API key not configured" error**
   - Make sure you have a `.env` file with your OpenAI API key
   - Verify the key is valid and has sufficient credits

2. **"Module not found" errors**
   - Ensure you've activated your virtual environment
   - Run `pip install -r requirements.txt` to install dependencies

3. **Flask app not starting**
   - Check if port 5000 is already in use
   - Try changing the port in `flask_app.py`

4. **Streamlit app issues**
   - Make sure Streamlit is installed: `pip install streamlit`
   - Try running with: `streamlit run app.py --server.port 8502`

### Getting Help

- Check the console output for detailed error messages
- Ensure all dependencies are installed correctly
- Verify your OpenAI API key is valid and active

## Disclaimer

⚠️ **Important Medical Disclaimer**: This AI assistant is for general health information only and should not replace professional medical advice. Always consult qualified healthcare professionals for medical concerns, diagnosis, or treatment.

## 🌟 Demo

Try the **standalone version** right now:
1. Download `standalone_chatbot.html`
2. Open it in your browser
3. Start chatting with demo responses!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### How to Contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- OpenAI for providing the GPT-3.5 Turbo API
- Flask community for the excellent web framework
- All contributors who help improve this project

---

**Built with ❤️ using Flask, OpenAI, and modern web technologies**

**MediAssist** - Your AI-powered healthcare companion, guiding you toward better health every day.
