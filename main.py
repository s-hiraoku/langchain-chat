from page_config import init_page
from model_selection import select_model
from messages import init_messages
from chat_interaction import handle_chat_interaction
from config import setup_env
from page_select import page_select


def main():
    setup_env()
    init_page()

    page_select()

    llm = select_model()

    init_messages()
    handle_chat_interaction(llm)


if __name__ == "__main__":
    main()
