from dotenv import load_dotenv
import os


def setup_env():
    """環境変数をロードする"""
    load_dotenv()


def get_openai_api_key():
    """OPENAI_API_KEY を取得する"""
    return os.getenv("OPENAI_API_KEY")
