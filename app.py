import streamlit as st
import ollama

st.title("My AI Chatbot")

prompt = st.text_input("Ask Something")

if st.button("Send"):
    if prompt.strip():
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.write(response["message"]["content"])
    else:
        st.warning("Please enter a message!")