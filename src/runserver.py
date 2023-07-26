from chatglm2_6b.modelClient import ChatGLM2
from chatglm2_6b.server import runserver
from config import Settings

chat_glm2 = ChatGLM2(Settings.CHATGLM_MODEL_PATH)


if __name__ == "__main__":
    runserver(chat_glm2)
