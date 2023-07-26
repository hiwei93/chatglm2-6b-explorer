from concurrent import futures

import grpc

from chatglm2_6b.grpc_pkg import chatglm_pb2_grpc, chatglm_pb2, utils


class ChatGLM2RPCServicer(chatglm_pb2_grpc.ChatGLM2RPCServicer):
    def __init__(self, model_client):
        self.model_client = model_client

    def Greet(self, request: chatglm_pb2.GreetRequest, context):
        text = f"hello, {request.name}"
        return chatglm_pb2.GenerateResponse(generated_text=text)

    def Generate(self, request: chatglm_pb2.GenerateRequest, context):
        text = self.model_client.generate(
            prompt=request.prompt,
            do_sample=request.do_sample,
            max_length=request.max_length,
            temperature=request.temperature,
            top_p=request.top_p,
        )
        return chatglm_pb2.GenerateResponse(generated_text=text)

    def StreamGenerate(self, request: chatglm_pb2.GenerateRequest, context):
        stream = self.model_client.stream_generate(
            prompt=request.prompt,
            do_sample=request.do_sample,
            max_length=request.max_length,
            temperature=request.temperature,
            top_p=request.top_p,
        )
        for text in stream:
            yield chatglm_pb2.GenerateResponse(generated_text=text)

    def StreamChat(self, request: chatglm_pb2.ChatRequest, context):
        history = utils.history2list(request.history)
        stream = self.model_client.stream_chat(
            query=request.query,
            history=history,
            max_length=request.max_length,
            do_sample=request.do_sample,
            top_p=request.top_p,
            temperature=request.temperature,
        )
        for text, new_history in stream:
            yield chatglm_pb2.ChatResponse(
                generated_text=text,
                new_history=utils.list2history(new_history),
            )


def run_grpc_server(model_client):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatglm_pb2_grpc.add_ChatGLM2RPCServicer_to_server(
        ChatGLM2RPCServicer(model_client), server
    )
    server.add_insecure_port('[::]:10002')
    print("grpc server is running on 10002 ...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    from chatglm2_6b.modelClient import FakeModelClient
    run_grpc_server(FakeModelClient())
