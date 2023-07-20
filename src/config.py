import os


class Settings:
    CHAT_CLIENT = os.environ.get("CHAT_CLIENT", "ChatGLM2APIClient")
    MODEL_WS_URL = os.environ.get("MODEL_WS_URL", "ws://localhost:10001")
    CHATGLM_MODEL_PATH = os.environ.get("CHATGLM_MODEL_PATH", "THUDM/chatglm2-6b")
