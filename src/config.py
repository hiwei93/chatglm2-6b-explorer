import os


class Settings:
    SERVER_TYPE = os.environ.get("SERVER_TYPE", "grpc")  # or websocket
    CHAT_CLIENT = os.environ.get("CHAT_CLIENT", "ChatGLM2GRPCClient")
    MODEL_WS_URL = os.environ.get("MODEL_WS_URL", "ws://localhost:10001")
    MODEL_GRPC_TARGET = os.environ.get("MODEL_GRPC_TARGET", "localhost:10002")
    CHATGLM_MODEL_PATH = os.environ.get("CHATGLM_MODEL_PATH", "THUDM/chatglm2-6b")
