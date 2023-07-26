#!/usr/bin/env bash

set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src/ --exclude='__init__.py,*_pb2.py,*_pb2_grpc.py'
black --exclude='.*_pb2_grpc.py|.*_pb2.py|.*_pb2.pyi' src/
isort --skip=chatglm_pb2.py --skip=chatglm_pb2.pyi --skip=chatglm_pb2_grpc.py src/
