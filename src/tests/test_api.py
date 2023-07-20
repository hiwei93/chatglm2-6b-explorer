from fastapi import WebSocketDisconnect
from fastapi.testclient import TestClient

from chatglm2_6b.server import app

client = TestClient(app)


def test_stream_generate():
    with client.websocket_connect("/streamGenerate") as websocket:
        websocket.send_json({"prompt": "问: 你好!\n答:", "temperature": 0.1})
        try:
            while True:
                data = websocket.receive_json()
        except WebSocketDisconnect:
            print("generation is finished")
        finally:
            assert data == {"text": "你好!请问有什么需要帮助的吗?"}
            print(data)


def test_generate():
    response = client.post(
        "/generate", json={"prompt": "问: 你好!\n答:", "temperature": 0.1}
    )
    data = response.json()
    print(data)
    assert data == {"text": "你好!请问有什么需要帮助的吗?"}


def test_stream_chat():
    with client.websocket_connect("/streamChat") as websocket:
        websocket.send_json({"query": "你好", "history": []})
        data = None
        try:
            while True:
                data = websocket.receive_json()
        except WebSocketDisconnect:
            print("generation is finished")
        finally:
            print(data)


if __name__ == "__main__":
    test_stream_generate()
    test_generate()
    test_stream_chat()
