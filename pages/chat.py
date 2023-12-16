import streamlit as st
from chat_interaction import handle_chat_interaction
from model_selection import select_model
from messages import init_messages

st.set_page_config(
    page_title="Chat",
    page_icon="🤗",
)

st.title("Chat 🤗")

llm = select_model()
handle_chat_interaction(llm)
init_messages()
