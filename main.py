import streamlit as st
from dotenv import load_dotenv
import os

from config import setup_env
from chat import handle_chat_interaction, init_messages
from sidebar import setup_sidebar


def setup_page():
    """ページの基本設定を行う関数"""
    st.set_page_config(page_title="My Great ChatGPT", page_icon="🤗")
    st.header("My Great ChatGPT 🤗")


def main():
    """メイン関数"""
    # ページの基本設定
    setup_page()
    setup_env()
    setup_sidebar()

    # チャット履歴の初期化
    init_messages()

    # チャット機能
    handle_chat_interaction()


if __name__ == "__main__":
    main()
