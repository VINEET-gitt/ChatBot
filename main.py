import streamlit as st
from groq import Groq

# Initialize Groq client (key stored securely in .streamlit/secrets.toml)
client = Groq(api_key = st.secrets["GROQ_API_KEY"])

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def ask_ai(messages):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content

# Render existing chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Show a welcome header only when there is no chat history
if not st.session_state.chat_history:
    st.markdown("<h2 style='text-align: center;'>Ask anything you want...</h2>", unsafe_allow_html=True)

# Chat input field
prompt = st.chat_input(placeholder = "What's in your mind...?")

if prompt:
    # 1. Append and display user message
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 2. Append and display assistant response (with conversation history)
    with st.chat_message("assistant"):
        reply = ask_ai(st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.write(reply)

with st.sidebar:
    st.title("Socials")
    st.link_button(label = "Instagram", url = "https://www.instagram.com/_k.vineettt?igsh=aXNpNzJpd2Ewb280", icon = "🔗")
    st.link_button(label = "G-mail", url = "mailto:vineet.29.work@gmail.com", icon = "🔗")