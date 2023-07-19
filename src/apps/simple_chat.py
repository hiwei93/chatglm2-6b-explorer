import gradio as gr
from chatClient import ChatClient
import traceback
from apps.components import chat_accordion

BOT_NAME = "ChatGLM2-6B"
TITLE = """<h3 align="center">🤖 通用对话</h3>"""
RETRY_COMMAND = "/retry"


def chat(client: ChatClient):
    with gr.Row():
        with gr.Column(elem_id="chat_container", scale=3):
            with gr.Row():
                chatbot = gr.Chatbot(elem_id="chatbot")
            with gr.Row():
                inputs = gr.Textbox(
                    placeholder=f"你好 {BOT_NAME} !",
                    label="输入内容后点击回车",
                    max_lines=3,
                )
            with gr.Row(elem_id="button_container"):
                with gr.Column():
                    retry_button = gr.Button("♻️ 重试上一轮对话")
                with gr.Column():
                    delete_turn_button = gr.Button("🧽 删除上一轮对话")
                with gr.Column():
                    clear_chat_button = gr.Button("✨ 删除全部对话历史")

        with gr.Column(elem_id="param_container", scale=1):
            temperature, top_p = chat_accordion()

    def run_chat(message: str, chat_history, temperature: float, top_p: float):
        if not message or (message == RETRY_COMMAND and len(chat_history) == 0):
            yield chat_history
            return

        if message == RETRY_COMMAND and chat_history:
            prev_turn = chat_history.pop(-1)
            user_message, _ = prev_turn
            message = user_message

        # chat_history = chat_history + [[message, ""]]
        try:
            stream = client.simple_chat(
                message,
                chat_history,
                temperature=temperature,
                top_p=top_p,
            )
            for resp, history in stream:
                chat_history = history
                yield chat_history
        except Exception as e:
            if not chat_history:
                chat_history = []
            chat_history += [["有错误了", traceback.format_exc()]]
            yield chat_history

    def delete_last_turn(chat_history):
        if chat_history:
            chat_history.pop(-1)
        return {chatbot: gr.update(value=chat_history)}

    def run_retry(message: str, chat_history, temperature: float, top_p: float):
        yield from run_chat(RETRY_COMMAND, chat_history, temperature, top_p)

    def clear_chat():
        return []

    inputs.submit(
        run_chat,
        [inputs, chatbot, temperature, top_p],
        outputs=[chatbot],
        show_progress=False,
    )
    inputs.submit(lambda: "", inputs=None, outputs=inputs)
    delete_turn_button.click(delete_last_turn, inputs=[chatbot], outputs=[chatbot])
    retry_button.click(
        run_retry,
        [inputs, chatbot, temperature, top_p],
        outputs=[chatbot],
        show_progress=False,
    )
    clear_chat_button.click(clear_chat, [], chatbot)


def simple_chat_demo(client: ChatClient):
    gr.HTML(TITLE)
    chat(client)
