import streamlit as st
import ollama
#Page Configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤦‍♀️"
)
#Title 
st.title("MY AI CHATBOT")
st.caption("powered by ollama+streamlit")
#initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages=[] 
#Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
#chat input
prompt=st.chat_input("type your message.....")
if prompt:
    #store user message
    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )
    #display user message
    with st.chat_message("user"):
        st.write(prompt)
    #get response from ollama
    response = ollama.chat(
                model="llama3.2",
                messages=st.session_state.messages

            )
    answer=response["message"]["content"]
    #store ai response
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer

        }
    )
    #Display ai response
    with st.chat_message("assistant"):
        st.write(answer)


