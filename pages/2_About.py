import streamlit as st

st.title("Welcome!!!")
st.header("This is the ultimately basic chatbot made by VINEET⚡ using Streamlit in Python.")
st.subheader("Source code:")
st.code('''
    # Main chatbot code
    import streamlit as st
    from groq import Groq

    # Initialize Groq client
    client = Groq(api_key = "YOUR_API_KEY_HERE")

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

    # History page code (pages/1_History.py)
    import streamlit as st

    st.header("Peek into your chat history...")
    if "chat_history" in st.session_state:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
''')

st.markdown('''
    NOTE: In future I might add some additional features like file uploading, voice search, etc.
''')