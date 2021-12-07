#!/bin/bash

# Cleanup
echo removing older protogen
rm -rf ./src/logic/protogen
mkdir ./src/logic/protogen

# Protogen
echo generating protogen
python -m grpc_tools.protoc -I./proto --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ./proto/warehouse/store.proto

echo Ok