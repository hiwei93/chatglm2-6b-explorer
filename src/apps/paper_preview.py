import traceback

import gradio as gr

from apps.components import chat_accordion

IDEA_TITLE = "论文速览"

prompt_tmpl = """下面是一篇论文的标题和摘要，请从以下几个方面进行总结：

1. 介绍本文的主要工作
2. 本文工作的主要亮点
3. 核心关键词（最多5个技术，能够代表本文核心技术，格式：`英文` (`中文`) ）
4. 从实用性、创新性和推荐度进行打分（各项满分5分）。

===
标题：{title}
===
摘要：{abstract}
===

注意：生成内容要简练，语言的组织要通顺、容易阅读和理解，并能够快速获取信息。
"""


def paper_preview_demo(client):
    def preview(title, abstract, temperature, top_p):
        if not title or not abstract:
            return None
        content = prompt_tmpl.format(title=title, abstract=abstract)
        try:
            stream = client.simple_chat(
                content,
                [],
                temperature=temperature,
                top_p=top_p,
            )
            for resp, _ in stream:
                pass
            return resp
        except Exception:
            return traceback.format_exc()

    with gr.Row():
        with gr.Column():
            title = gr.Textbox(label="论文标题")
            abstract = gr.Textbox(label="摘要", lines=5)
            with gr.Row():
                with gr.Column():
                    submit = gr.Button("速览", variant="primary")
                with gr.Column():
                    clear = gr.Button("清空")
            temperature, top_p = chat_accordion()

        with gr.Column():
            outputs = gr.Textbox(label="速览内容", lines=5)

        submit.click(
            preview, inputs=[title, abstract, temperature, top_p], outputs=outputs
        )
        clear.click(lambda x: (None, None), inputs=None, outputs=[title, abstract])
