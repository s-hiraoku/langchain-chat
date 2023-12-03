import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

from config import get_openai_api_key


def select_model():
    """モデル選択と設定のための関数"""
    openai_api_key = get_openai_api_key()

    model = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
    model_name = "gpt-3.5-turbo-0613" if model == "GPT-3.5" else "gpt-4"

    temperature = st.sidebar.slider(
        "Temperature:", min_value=0.0, max_value=2.0, value=0.0, step=0.01
    )

    return ChatOpenAI(
        temperature=temperature, model_name=model_name, openai_api_key=openai_api_key
    )


def init_messages():
    """チャットメッセージの初期化"""
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button or "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]


def handle_chat_interaction():
    """チャットインタラクションの処理"""
    llm = select_model()

    # ユーザーの入力を監視
    if user_input := st.chat_input("聞きたいことを入力してね！"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("ChatGPT is typing ..."):
            response = llm(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    # チャット履歴の表示
    messages = st.session_state.get("messages", [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        else:  # SystemMessage
            st.write(f"System message: {message.content}")
