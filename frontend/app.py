import streamlit as st
import requests

st.set_page_config(
    page_title="GenAI RAG Assistant",
    page_icon="🤖"
)

st.title("🤖 GenAI RAG Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("Ask a question")

if st.button("Send") and user_input:

    payload = {
        "sessionId": "user123",
        "message": user_input
    }

    try:
        with st.spinner("Thinking..."):

            response = requests.post(
                "http://127.0.0.1:8000/api/chat",
                json=payload
            )

            data = response.json()

            reply = data["reply"]

            # Save messages
            st.session_state.messages.append(
                {"role": "user", "content": user_input}
            )

            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Display chat history
for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(f"### 👤 You")
        st.write(message["content"])

    else:
        st.markdown(f"### 🤖 Assistant")
        st.write(message["content"])