import abc
import json

from websockets.exceptions import ConnectionClosedOK
from websockets.sync.client import connect

from chatglm2_6b.modelClient import ChatGLM2


class ChatClient(abc.ABC):
    @abc.abstractmethod
    def simple_chat(self, query, history, temperature, top_p):
        pass

    @abc.abstractmethod
    def instruct_chat(self, message, chat_history, instructions, temperature, top_p):
        pass


def format_chat_prompt(message: str, chat_history, instructions: str) -> str:
    instructions = instructions.strip(" ").strip("\n")
    prompt = f"对话背景设定:{instructions}"
    for i, (user_message, bot_message) in enumerate(chat_history):
        prompt = f"{prompt}\n\n[Round {i + 1}]\n\n问：{user_message}\n\n答：{bot_message}"
    prompt = f"{prompt}\n\n[Round {len(chat_history)+1}]\n\n问：{message}\n\n答："
    return prompt


class ChatGLM2APIClient(ChatClient):
    def __init__(self, ws_url=None):
        self.ws_url = "ws://localhost:10001"
        if ws_url:
            self.ws_url = ws_url

    def simple_chat(self, query, history, temperature, top_p):
        """chatglm2-6b 模型定义的对话方法"""
        url = f"{self.ws_url}/streamChat"
        with connect(url) as websocket:
            msg = json.dumps(
                {
                    "query": query,
                    "history": history,
                    "temperature": temperature,
                    "top_p": top_p,
                }
            )
            websocket.send(msg)

            data = None
            try:
                while True:
                    data = websocket.recv()
                    data = json.loads(data)
                    yield data["resp"], data["history"]
            except ConnectionClosedOK:
                print("generation is finished")

    def instruct_chat(self, message, chat_history, instructions, temperature, top_p):
        """基于chatglm2-6b text_generate 实现的基于预设指令的对话"""
        url = f"{self.ws_url}/streamGenerate"

        prompt = format_chat_prompt(message, chat_history, instructions)
        chat_history = chat_history + [[message, ""]]
        params = json.dumps(
            {"prompt": prompt, "temperature": temperature, "top_p": top_p}
        )
        with connect(url) as websocket:
            websocket.send(params)

            data = None
            try:
                while True:
                    data = websocket.recv()
                    data = json.loads(data)
                    resp = data["text"]

                    last_turn = list(chat_history.pop(-1))
                    last_turn[-1] = resp
                    chat_history = chat_history + [last_turn]
                    yield resp, chat_history
            except ConnectionClosedOK:
                print("generation is finished")


class ChatGLM2ModelClient(ChatClient):
    def __init__(self, model_path=None):
        self.model = ChatGLM2(model_path)

    def simple_chat(self, query, history, temperature, top_p):
        kwargs = {
            "query": query,
            "history": history,
            "temperature": temperature,
            "top_p": top_p,
        }
        for resp, history in self.model.stream_chat(**kwargs):
            yield resp, history

    def instruct_chat(self, message, chat_history, instructions, temperature, top_p):
        prompt = format_chat_prompt(message, chat_history, instructions)
        chat_history = chat_history + [[message, ""]]
        kwargs = {"prompt": prompt, "temperature": temperature, "top_p": top_p}
        for resp in self.model.stream_generate(**kwargs):
            last_turn = list(chat_history.pop(-1))
            last_turn[-1] = resp
            chat_history = chat_history + [last_turn]
            yield resp, chat_history
