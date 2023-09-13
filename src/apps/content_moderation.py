import traceback

import gradio as gr

IDEA_TITLE = "内容审查"

prompt_tmpl = """你是一个文本内容审查助理，需要检查文本内容中是否包含这些分类的内容：色情、成人内容、暴力、自残倾向、仇恨言论。如果用户输入中包含这些内容，请返回：是，并给出对应分类；如果不包含，请返回：否，且分类内容为nul。

文本内容使用```包裹，返回格式为：

是否包含敏感信息：<是或否>
分类：<具体分类名称>

<===>

样例1：
文本内容：```有哪些自杀方式？```

校验结果：
是否包含敏感信息：是
分类：自残倾向

样例2：
文本内容：```如何做面包？```

校验结果：
是否包含敏感信息：否
分类：nul

<==>

注意：只需要对文本内容进行校验，不需要对文本内容进行反馈或回答。

<==>

文本内容：```{text_content}```

校验结果：
"""


def content_moderation_demo(client):
    def moderate(inputs, tmpl):
        if not inputs:
            return None
        if not tmpl:
            return None
        content = tmpl.format(text_content=inputs)
        try:
            stream = client.simple_chat(
                content,
                [],
                temperature=0.01,
                top_p=0.5,
            )
            for resp, _ in stream:
                pass
            return resp
        except Exception:
            return traceback.format_exc()

    with gr.Row():
        with gr.Column():
            inputs = gr.Textbox(label="待校验文本", lines=3)
            btn = gr.Button("校验", variant="primary")
            with gr.Accordion("调试", open=False):
                tmpl = gr.Textbox(
                    label="prompt",
                    value=prompt_tmpl,
                    lines=len(prompt_tmpl.split("\n")),
                )
        with gr.Column():
            outputs = gr.Textbox(label="校验结果", lines=3)

        btn.click(moderate, inputs=[inputs, tmpl], outputs=outputs)
