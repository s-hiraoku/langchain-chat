import streamlit as st


def chat_page():
    st.title("My Great ChatGPT 🤗")


def url_input_page():
    st.title("URL")


def page_select():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page:", ("Chat", "Request URL"))

    if page == "Chat":
        chat_page()
    elif page == "Request URL":
        url_input_page()
