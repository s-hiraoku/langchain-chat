from page_config import init_page
from model_selection import select_model
from messages import init_messages
from config import setup_env
from page_select import page_select, select_page
from chat_interaction import handle_chat_interaction
from web_summarize import handle_web_summarize


def main():
    setup_env()
    init_page()

    page = page_select()
    llm = select_model()

    if page == select_page["chat"]:
        handle_chat_interaction(llm)
    elif page == select_page["webSite"]:
        handle_web_summarize(llm)

    init_messages()


if __name__ == "__main__":
    main()
