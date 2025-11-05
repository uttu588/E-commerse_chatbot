import streamlit as st
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import your chatbot logic (example from App/main.py)
from App import main

st.set_page_config(page_title="E-commerce Chatbot", page_icon="🛍️")

st.title("🛍️ E-commerce Chatbot")

user_input = st.text_input("You:", "")

if st.button("Ask"):
    if user_input.strip():
        response = main.chatbot_response(user_input)  # Replace with your chatbot's main function
        st.write(f"🤖 Bot: {response}")
    else:
        st.warning("Please enter a question.")
