import streamlit as st
from model_selection import select_model
from pdf_knowledge_base import handle_pdf_knowledge_base

st.set_page_config(
    page_title="PDF Knowledge",
    page_icon="📚",
)

st.title("PDF Knowledge 📚")
llm = select_model()
handle_pdf_knowledge_base(llm)
