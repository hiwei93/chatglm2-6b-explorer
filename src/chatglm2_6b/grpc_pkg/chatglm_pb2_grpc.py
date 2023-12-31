# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chatglm2_6b.grpc_pkg.chatglm_pb2 as chatglm__pb2


class ChatGLM2RPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Greet = channel.unary_unary(
                '/ChatGLM2RPC/Greet',
                request_serializer=chatglm__pb2.GreetRequest.SerializeToString,
                response_deserializer=chatglm__pb2.GenerateResponse.FromString,
                )
        self.Generate = channel.unary_unary(
                '/ChatGLM2RPC/Generate',
                request_serializer=chatglm__pb2.GenerateRequest.SerializeToString,
                response_deserializer=chatglm__pb2.GenerateResponse.FromString,
                )
        self.StreamGenerate = channel.unary_stream(
                '/ChatGLM2RPC/StreamGenerate',
                request_serializer=chatglm__pb2.GenerateRequest.SerializeToString,
                response_deserializer=chatglm__pb2.GenerateResponse.FromString,
                )
        self.StreamChat = channel.unary_stream(
                '/ChatGLM2RPC/StreamChat',
                request_serializer=chatglm__pb2.ChatRequest.SerializeToString,
                response_deserializer=chatglm__pb2.ChatResponse.FromString,
                )


class ChatGLM2RPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Greet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Generate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamGenerate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatGLM2RPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Greet': grpc.unary_unary_rpc_method_handler(
                    servicer.Greet,
                    request_deserializer=chatglm__pb2.GreetRequest.FromString,
                    response_serializer=chatglm__pb2.GenerateResponse.SerializeToString,
            ),
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=chatglm__pb2.GenerateRequest.FromString,
                    response_serializer=chatglm__pb2.GenerateResponse.SerializeToString,
            ),
            'StreamGenerate': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamGenerate,
                    request_deserializer=chatglm__pb2.GenerateRequest.FromString,
                    response_serializer=chatglm__pb2.GenerateResponse.SerializeToString,
            ),
            'StreamChat': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamChat,
                    request_deserializer=chatglm__pb2.ChatRequest.FromString,
                    response_serializer=chatglm__pb2.ChatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ChatGLM2RPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatGLM2RPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Greet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ChatGLM2RPC/Greet',
            chatglm__pb2.GreetRequest.SerializeToString,
            chatglm__pb2.GenerateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ChatGLM2RPC/Generate',
            chatglm__pb2.GenerateRequest.SerializeToString,
            chatglm__pb2.GenerateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamGenerate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ChatGLM2RPC/StreamGenerate',
            chatglm__pb2.GenerateRequest.SerializeToString,
            chatglm__pb2.GenerateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ChatGLM2RPC/StreamChat',
            chatglm__pb2.ChatRequest.SerializeToString,
            chatglm__pb2.ChatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
