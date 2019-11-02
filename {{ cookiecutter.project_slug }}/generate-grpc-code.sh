#!/bin/env bash

cd protos
for proto_file in ./proto/*.proto; do
    echo "Generating gRPC code for ${proto_file}"
    python -m grpc_tools.protoc -I . --python_out=./python --grpc_python_out=./python ${proto_file}
done
