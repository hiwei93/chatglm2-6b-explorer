#!/usr/bin/env bash

set -x

mypy --exclude='grpc_pkg' src/
black --check --exclude='.*_pb2_grpc.py|.*_pb2.py|.*_pb2.pyi' src/
isort --check-only --skip=chatglm_pb2.py --skip=chatglm_pb2.pyi --skip=chatglm_pb2_grpc.py src/
flake8 --max-line-length=88 --extend-ignore=E203 --exclude='__init__.py,*_pb2.py,*_pb2_grpc.py,*_pb2.pyi'