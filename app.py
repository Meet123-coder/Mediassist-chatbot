import streamlit as st
from chatbot import get_healthcare_response

st.set_page_config(page_title="Healthcare Chatbot", page_icon="🩺")

st.title("Healthcare Chatbot 🤖 (OpenAI GPT-3.5)")

# Store conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar for controls
with st.sidebar:
    st.header("Chat Controls")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", help="Clear all conversation history"):
        st.session_state.history = []
        st.success("Chat cleared successfully!")
        st.rerun()
    
    # Show chat statistics
    if st.session_state.history:
        st.metric("Messages", len(st.session_state.history))
        st.metric("User Messages", len([h for h in st.session_state.history if h.get("user")]))
        st.metric("Bot Responses", len([h for h in st.session_state.history if h.get("bot")]))
    
    # Download chat history
    if st.session_state.history:
        chat_text = ""
        for chat in st.session_state.history:
            chat_text += f"User: {chat['user']}\n"
            chat_text += f"Bot: {chat['bot']}\n"
            chat_text += "---\n"
        
        st.download_button(
            label="📥 Download Chat",
            data=chat_text,
            file_name="healthcare_chat_history.txt",
            mime="text/plain"
        )

# Main chat interface
col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input("Ask me about your health:", placeholder="Type your health question here...", key="user_input")

with col2:
    send_button = st.button("Send", type="primary", use_container_width=True)

# Process message
if (send_button or user_input) and user_input.strip():
    with st.spinner("Thinking..."):
        reply = get_healthcare_response(user_input)
        st.session_state.history.append({"user": user_input, "bot": reply})
        st.rerun()

# Display conversation
if st.session_state.history:
    st.markdown("### Conversation History")
    
    for i, chat in enumerate(st.session_state.history):
        with st.expander(f"Message {i+1}", expanded=True):
            st.markdown(f"**👤 You:** {chat['user']}")
            st.markdown(f"**🤖 Bot:** {chat['bot']}")
else:
    st.info("👋 Hello! I'm your AI healthcare assistant. I can help answer general health questions and provide health information. What would you like to know?")
    st.warning("⚠️ This is an AI assistant for general health information only. Always consult healthcare professionals for medical advice.")
