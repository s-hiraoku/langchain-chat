import streamlit as st
from web_summarize import handle_web_summarize
from model_selection import select_model


st.set_page_config(
    page_title="Web Site Summarizer",
    page_icon="🔗",
)

st.title("Web Site Summarizer 🔗")

llm = select_model()
handle_web_summarize(llm)
