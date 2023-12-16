import streamlit as st
from model_selection import select_model
from youtube_summarize import chain_type_select, handle_youtube_summarize


st.set_page_config(
    page_title="Youtube Video Summarizer",
    page_icon="📺",
)

st.title("Youtube Video Summarizer 📺")

llm = select_model()
chain_type = chain_type_select()
handle_youtube_summarize(llm, chain_type)
