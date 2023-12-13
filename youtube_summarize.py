import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import YoutubeLoader
import ssl


def get_url_input():
    url = st.text_input("Youtube URL: ", key="input")
    return url


def get_document(url):
    with st.spinner("Fetching Content ..."):
        ssl._create_default_https_context = ssl._create_unverified_context
        loader = YoutubeLoader.from_youtube_url(
            url,
            add_video_info=True,  # タイトルや再生数も取得できる
            language=["en", "ja"],  # 英語→日本語の優先順位で字幕を取得
        )
        return loader.load()


def summarize(llm, docs):
    prompt_template = """Write a concise Japanese summary of the following transcript of Youtube Video.

============

{text}

============

ここから日本語で書いてね
必ず3段落以内の200文字以内で簡潔にまとめること:
"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])

    with get_openai_callback() as cb:
        chain = load_summarize_chain(
            llm, chain_type="stuff", verbose=True, prompt=PROMPT
        )
        response = chain({"input_documents": docs}, return_only_outputs=True)

    return response["output_text"], cb.total_cost


def handle_youtube_summarize(llm):
    container = st.container()
    response_container = st.container()

    with container:
        url = get_url_input()
        if url:
            document = get_document(url)
            with st.spinner("ChatGPT is typing ..."):
                output_text, cost = summarize(llm, document)
            st.session_state.costs.append(cost)
        else:
            output_text = None

    if output_text:
        with response_container:
            st.markdown("## Summary")
            st.write(output_text)
            st.markdown("---")
            st.markdown("## Original Text")
            st.write(document)

    costs = st.session_state.get("costs", [])
    st.sidebar.markdown("## Costs")
    st.sidebar.markdown(f"**Total cost: ${sum(costs):.5f}**")
    for cost in costs:
        st.sidebar.markdown(f"- ${cost:.5f}")
