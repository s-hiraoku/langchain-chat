import streamlit as st


def page_select():
    page = st.sidebar.radio("Choose a page:", ("Chat", "Request URL"))
