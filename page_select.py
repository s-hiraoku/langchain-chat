import streamlit as st

select_page = {
    "chat": "Chat",
    "webSite": "Web Site Summarizer",
    "youtube": "Youtube Video Summarizer",
}


def chat_page():
    st.title("Chat 🤗")


def url_input_page():
    st.title("Web Site Summarizer 🔗")


def youtube_summary_page():
    st.title("Youtube Video Summarizer 📺")


def page_select():
    st.sidebar.title("Function Selection")
    page_key = st.sidebar.radio("Choose a function:", list(select_page.values()))

    if page_key == select_page["chat"]:
        chat_page()
    elif page_key == select_page["webSite"]:
        url_input_page()
    elif page_key == select_page["youtube"]:
        youtube_summary_page()

    return page_key
