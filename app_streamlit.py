# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Original file is located at
    https://colab.research.google.com/drive/1P5BjQYhdD3j9rbZu5GFF3QHJVhSYIhAO
"""

import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI HR Chatbot", layout="centered")

st.title("🤖 AI-Powered HR Chatbot")

# Input box
user_query = st.text_input("What kind of candidate are you looking for?", "")

if user_query:
    st.markdown("#### 🔍 Searching candidates...")
    
    # 🔮 MOCKED response (fake but realistic)
    response = f"""
✅ Based on your query: **"{user_query}"**, I found 2 strong matches:

• **Nina D'Souza** – 4 years in Machine Learning and Healthcare. Built *X-ray Scanner AI* and *Health Risk Monitor*. Currently available.

• **Clara Mendes** – 6 years experience. Led a *Medical Diagnosis Platform* using TensorFlow and PyTorch. Currently unavailable.

Would you like to explore their profiles or schedule a meeting?
"""
    st.success(response)
