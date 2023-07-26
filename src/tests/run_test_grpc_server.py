from chatglm2_6b.grpc_server import run_grpc_server
from chatglm2_6b.modelClient import FakeModelClient


if __name__ == '__main__':
    model_client = FakeModelClient()
    run_grpc_server(model_client)
