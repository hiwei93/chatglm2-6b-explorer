from chatglm2_6b.grpc_server import run_grpc_server
from chatglm2_6b.modelClient import ChatGLM2
from chatglm2_6b.server import runserver
from config import Settings

server_register = {
    "websocket": runserver,
    "grpc": run_grpc_server,
}


if __name__ == "__main__":
    chat_glm2 = ChatGLM2(Settings.CHATGLM_MODEL_PATH)
    server = server_register[Settings.SERVER_TYPE]
    server(chat_glm2)
