import streamlit as st
from dotenv import load_dotenv
import os
from goggle import genai




#get api key
api_key=os.getenv("GEMINI_API_KEY")
#Create gemini client
client = genai.Client(api_key=api_key)
#page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)
#title
st.title("")
