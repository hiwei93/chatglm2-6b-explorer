import gradio as gr

from apps import instruction_chat_demo, simple_chat_demo, translator_demo
from chatClient import ChatClient, ChatGLM2APIClient, ChatGLM2ModelClient
from config import Settings

TITLE = """<h2 align="center">🚀 ChatGLM2-6B apps gallery</h2>"""

demo_register = {
    "通用对话": simple_chat_demo,
    "预设指令对话": instruction_chat_demo,
    "翻译器": translator_demo,
}


def get_gallery(client: ChatClient):
    with gr.Blocks(
        # css=None
        # css="""#chat_container {width: 700px; margin-left: auto; margin-right: auto;}
        #        #button_container {width: 700px; margin-left: auto; margin-right: auto;}
        #        #param_container {width: 700px; margin-left: auto; margin-right: auto;}"""
        css="""#chatbot {
            font-size: 14px;
            min-height: 300px;
        }"""
    ) as demo:
        gr.HTML(TITLE)
        for name, demo_func in demo_register.items():
            with gr.Tab(name):
                demo_func(client)
    return demo


def build_client():
    client_class = Settings.CHAT_CLIENT
    if client_class == "ChatGLM2ModelClient":
        return ChatGLM2ModelClient(Settings.CHATGLM_MODEL_PATH)
    if client_class == "ChatGLM2APIClient":
        return ChatGLM2APIClient(Settings.MODEL_WS_URL)
    raise Exception(f"Wrong ChatClient: {client_class}")


if __name__ == "__main__":
    client = build_client()
    demo = get_gallery(client)
    demo.queue(max_size=128, concurrency_count=16)
    demo.launch()
