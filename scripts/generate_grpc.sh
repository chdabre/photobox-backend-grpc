#!/bin/sh

python -m grpc_tools.protoc -I ./protos --python_out=./photobox_backend_grpc --pyi_out=./photobox_backend_grpc --grpc_python_out=./photobox_backend_grpc ./protos/photobox_service.proto
