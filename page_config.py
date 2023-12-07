import streamlit as st


def init_page():
    st.set_page_config(page_title="My Great ChatGPT", page_icon="🤗")
    st.header("My Great ChatGPT 🤗")
    st.sidebar.title("Options")


def init_url_page():
    st.set_page_config(page_title="Website Summarizer", page_icon="🤗")
    st.header("Website Summarizer 🤗")
    st.sidebar.title("Options")
