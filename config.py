from dotenv import load_dotenv
import os


def setup_env():
    load_dotenv()


def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")
