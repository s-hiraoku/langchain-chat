import streamlit as st
from langchain.chat_models import ChatOpenAI
from config import get_openai_api_key


def select_model():
    openai_api_key = get_openai_api_key()
    model = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
    model_name = "gpt-3.5-turbo" if model == "GPT-3.5" else "gpt-4"
    temperature = st.sidebar.slider(
        "Temperature:", min_value=0.0, max_value=2.0, value=0.0, step=0.01
    )
    return ChatOpenAI(
        temperature=temperature,
        model_name=model_name,
        openai_api_key=openai_api_key,
        streaming=True,
    )
