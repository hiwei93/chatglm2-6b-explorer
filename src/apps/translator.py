import traceback

import gradio as gr

from apps.components import chat_accordion

IDEA_TITLE = "ChatGLM2-6B 翻译官"

prompt_tmpl = """imagine you are a professional translator. Your task is translating the text around by ``` to Chinese.

input text：

```
{input_text}
```

translation result:"""


def translator_demo(client):
    def stream_translate(input_text, temperature: float, top_p: float):
        if not input_text:
            return None
        message = prompt_tmpl.format(input_text=input_text)
        try:
            stream = client.simple_chat(
                message,
                [],
                temperature=temperature,
                top_p=top_p,
            )
            for resp, _ in stream:
                pass
            return resp
        except Exception:
            return traceback.format_exc()

    def clear_content():
        return None, None

    with gr.Row():
        with gr.Column():
            inputs = gr.Textbox(label="请输入原文", max_lines=5)
            gr.Dropdown(["en -> zh"], value="en -> zh", label="翻译语言")
            temperature, top_p = chat_accordion()
            with gr.Row(elem_id="button_container"):
                with gr.Column():
                    commit_btn = gr.Button(value="翻译", variant="primary")
                with gr.Column():
                    clear_btn = gr.Button(value="清空")

        with gr.Column():
            outputs = gr.Textbox(label="译文", max_lines=5)

        commit_btn.click(
            stream_translate, inputs=[inputs, temperature, top_p], outputs=[outputs]
        )
        clear_btn.click(clear_content, inputs=None, outputs=[inputs, outputs])
