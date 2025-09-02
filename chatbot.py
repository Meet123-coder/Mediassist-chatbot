import openai
import logging
from typing import Optional
from config import config

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format=config.LOG_FORMAT
)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
if not config.OPENAI_API_KEY:
    logger.warning("OpenAI API key not found in environment variables")
    client = None
else:
    client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

def get_healthcare_response(user_input: str) -> str:
    """
    Get healthcare response from OpenAI GPT model.
    
    Args:
        user_input (str): User's healthcare question or message
        
    Returns:
        str: AI response or error message
    """
    try:
        # Input validation
        if not user_input or not isinstance(user_input, str):
            return "Please enter a valid healthcare question."
            
        user_input = user_input.strip()
        if not user_input:
            return "Please enter a valid healthcare question."
            
        # Check if input is too long
        if len(user_input) > config.MAX_MESSAGE_LENGTH:
            return f"Your message is too long. Please keep it under {config.MAX_MESSAGE_LENGTH} characters."
            
        # Check if client is initialized
        if not client:
            logger.error("OpenAI client not initialized - API key missing")
            return "Error: API key not configured. Please check your environment setup."
        
        # Log the request
        logger.info(f"Processing healthcare query: {user_input[:100]}...")
        
        response = client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful healthcare assistant. Provide accurate, helpful medical information while always reminding users to consult healthcare professionals for serious concerns. Keep responses concise and informative. Always include a disclaimer about consulting healthcare professionals for serious medical issues."
                },
                {"role": "user", "content": user_input}
            ],
            temperature=config.OPENAI_TEMPERATURE,
            max_tokens=config.OPENAI_MAX_TOKENS,
            timeout=config.OPENAI_TIMEOUT
        )
        
        response_text = response.choices[0].message.content.strip()
        logger.info(f"Generated response: {response_text[:100]}...")
        return response_text
        
    except openai.AuthenticationError:
        logger.error("OpenAI authentication failed")
        return "Error: Invalid API key. Please check your OpenAI API key configuration."
    except openai.RateLimitError:
        logger.error("OpenAI rate limit exceeded")
        return "Error: Rate limit exceeded. Please try again in a moment."
    except openai.APITimeoutError:
        logger.error("OpenAI API timeout")
        return "Error: Request timed out. Please try again."
    except openai.APIError as e:
        logger.error(f"OpenAI API error: {e}")
        return "Error: Unable to process your request. Please try again later."
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return "Error: An unexpected error occurred. Please try again."
