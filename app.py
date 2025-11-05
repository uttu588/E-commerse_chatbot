import streamlit as st
import sys, os

# ✅ Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# ✅ Import main from App package inside src
from App import main

st.set_page_config(page_title="E-commerce Chatbot", page_icon="🛍️")

st.title("🛍️ E-commerce Chatbot")

user_input = st.text_input("You:", "")

if st.button("Ask"):
    if user_input.strip():
        response = main.chatbot_response(user_input)  # Make sure chatbot_response exists in main.py
        st.write(f"🤖 Bot: {response}")
    else:
        st.warning("Please enter a question.")
