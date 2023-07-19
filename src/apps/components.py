import gradio as gr


def chat_accordion():
    with gr.Accordion("参数设置", open=False):
        temperature = gr.Slider(
            minimum=0.1,
            maximum=2.0,
            value=0.8,
            step=0.1,
            interactive=True,
            label="Temperature",
        )
        top_p = gr.Slider(
            minimum=0.1,
            maximum=0.99,
            value=0.9,
            step=0.01,
            interactive=True,
            label="top_p",
        )
    return temperature, top_p
