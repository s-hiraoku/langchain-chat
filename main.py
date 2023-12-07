from page_config import init_page, init_url_page
from model_selection import select_model
from messages import init_messages
from chat_interaction import handle_chat_interaction
from config import setup_env
from page_select import page_select


def main():
    setup_env()
    page = page_select()
    if page == "Chat":
        init_page()
        llm = select_model()
        init_messages()
        handle_chat_interaction(llm)
    elif page == "Request URL":
        init_url_page()
        llm = select_model()
        init_messages()


if __name__ == "__main__":
    main()
