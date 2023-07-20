from chatClient import ChatGLM2APIClient, ChatGLM2ModelClient


def test_api_client_simple_chat():
    client = ChatGLM2APIClient()
    stream = client.simple_chat("睡不着怎么办？", [], 0.7, 0.9)
    for resp, history in stream:
        r = resp
        print(r)
        print("*" * 50)


def test_model_client_simple_chat():
    client = ChatGLM2ModelClient()
    stream = client.simple_chat("睡不着怎么办？", [], 0.7, 0.9)
    for resp, history in stream:
        r = resp
        print(r)
        print("*" * 50)


if __name__ == "__main__":
    test_api_client_simple_chat()
    test_model_client_simple_chat()
