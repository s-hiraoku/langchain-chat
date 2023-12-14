from page_config import init_page
from model_selection import select_model
from messages import init_messages
from config import setup_env
from page_select import page_select, select_page
from chat_interaction import handle_chat_interaction
from web_summarize import handle_web_summarize
from youtube_summarize import handle_youtube_summarize, chain_type_select


def main():
    setup_env()
    init_page()

    page = page_select()
    llm = select_model()

    if page == select_page["chat"]:
        handle_chat_interaction(llm)
    elif page == select_page["webSite"]:
        handle_web_summarize(llm)
    elif page == select_page["youtube"]:
        chain_type = chain_type_select()
        handle_youtube_summarize(llm, chain_type)

    init_messages()


if __name__ == "__main__":
    main()
