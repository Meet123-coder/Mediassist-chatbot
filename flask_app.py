from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import get_healthcare_response
import logging
from config import config

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format=config.LOG_FORMAT
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages and return AI responses."""
    try:
        logger.info(f"Chat endpoint called with method: {request.method}")
        logger.info(f"Request headers: {dict(request.headers)}")
        
        # Validate request
        if not request.is_json:
            logger.error("Request is not JSON")
            return jsonify({'error': 'Content-Type must be application/json'}), 400
            
        data = request.get_json()
        logger.info(f"Request data: {data}")
        
        if not data:
            logger.error("No JSON data provided")
            return jsonify({'error': 'No JSON data provided'}), 400
            
        if 'message' not in data:
            logger.error("No message field in request")
            return jsonify({'error': 'No message field provided'}), 400
        
        user_message = data['message']
        if not isinstance(user_message, str):
            logger.error(f"Message is not a string: {type(user_message)}")
            return jsonify({'error': 'Message must be a string'}), 400
            
        user_message = user_message.strip()
        if not user_message:
            logger.error("Empty message received")
            return jsonify({'error': 'Empty message'}), 400
        
        # Log the request
        logger.info(f"Processing chat request: {user_message[:100]}...")
        
        # Get AI response
        ai_response = get_healthcare_response(user_message)
        
        logger.info(f"Generated response: {ai_response[:100]}...")
        
        response_data = {
            'reply': ai_response,
            'status': 'success'
        }
        
        logger.info(f"Returning response: {response_data}")
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}", exc_info=True)
        return jsonify({
            'error': 'Internal server error',
            'status': 'error'
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'service': 'healthcare-chatbot'})

@app.route('/test')
def test_endpoint():
    """Test endpoint for debugging."""
    try:
        from config import config
        return jsonify({
            'status': 'success',
            'message': 'Test endpoint working',
            'config_loaded': bool(config),
            'openai_configured': bool(config.OPENAI_API_KEY) if config else False
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    # Validate configuration
    if not config.validate_config():
        logger.error("Configuration validation failed. Please check your .env file.")
        exit(1)
    
    # Print configuration
    config.print_config()
    
    # Get Flask configuration
    flask_config = config.get_flask_config()
    
    logger.info(f"Starting Flask app on {flask_config['host']}:{flask_config['port']} (debug={flask_config['debug']})")
    app.run(
        debug=flask_config['debug'], 
        host=flask_config['host'], 
        port=flask_config['port']
    )
