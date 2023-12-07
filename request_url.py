import streamlit as st
import requests
from bs4 import BeautifulSoup


def get_content(url):
    try:
        with st.spinner("Fetching Content ..."):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            # fetch text from main (change the below code to filter page)
            if soup.main:
                return soup.main.get_text()
            elif soup.article:
                return soup.article.get_text()
            else:
                return soup.body.get_text()
    except:
        st.write("something wrong")
        return None


def build_prompt(content, n_chars=300):
    return f"""以下はとある。Webページのコンテンツである。内容を{n_chars}程度でわかりやすく要約してください。

========

{content[:1000]}

========

日本語で書いてね！
"""


with response_container:
    st.markdown("## Summary")
    st.write(answer)
    st.markdown("---")
    st.markdown("## Original Text")
    st.write(content)
