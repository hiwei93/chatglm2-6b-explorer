import grpc

from chatglm2_6b.grpc_pkg import chatglm_pb2_grpc, chatglm_pb2


def get_stub():
    channel = grpc.insecure_channel('localhost:10002')
    stub = chatglm_pb2_grpc.ChatGLM2RPCStub(channel)
    return stub


def test_greet():
    stub = get_stub()
    resp = stub.Greet(chatglm_pb2.GreetRequest(name="zhangwei"))
    print(resp.generated_text)


def test_generate():
    stub = get_stub()
    resp = stub.Generate(chatglm_pb2.GenerateRequest(
        prompt="你好",
        do_sample=True,
        max_length=2048,
        temperature=0.9,
        top_p=0.8,
    ))
    print(resp.generated_text)


def test_stream_generate():
    stub = get_stub()
    stream = stub.StreamGenerate(chatglm_pb2.GenerateRequest(
        prompt="你好",
        do_sample=True,
        max_length=2048,
        temperature=0.9,
        top_p=0.8,
    ))
    for resp in stream:
        print(resp.generated_text)


def test_stream_chat():
    stub = get_stub()
    stream = stub.StreamChat(chatglm_pb2.ChatRequest(
        query="你好",
        history=chatglm_pb2.ChatHistory(),
        do_sample=True,
        max_length=2048,
        temperature=0.9,
        top_p=0.8,
    ))
    for resp in stream:
        print([[s for s in turn.strings] for turn in resp.new_history.turns])


if __name__ == '__main__':
    test_stream_chat()
