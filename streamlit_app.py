import streamlit as st
import openai

# Set page config
st.set_page_config(page_title="Chatbot", page_icon="💬")

# Load API key from secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat UI
st.title("💬 Chatbot")
st.markdown("Talk to the chatbot using OpenAI GPT-3.5!")

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call OpenAI GPT-3.5
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )

    # Get assistant message
    assistant_message = response["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
