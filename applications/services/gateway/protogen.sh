#!/bin/bash

# Cleanup
echo removing older protogen...
rm -rf ./src/logic/protogen
mkdir ./src/logic/protogen

# Protogen
echo generating protogen...
python -m grpc_tools.protoc -I../../protos --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ../../protos/store.proto
python -m grpc_tools.protoc -I../../protos/subscription --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ../../protos/subscription/customer.proto
python -m grpc_tools.protoc -I../../protos/subscription --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ../../protos/subscription/subscription.proto
python -m grpc_tools.protoc -I../../protos/metadata --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ../../protos/metadata/book.proto
python -m grpc_tools.protoc -I../../protos/metadata --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ../../protos/metadata/song.proto
python -m grpc_tools.protoc -I../../protos/metadata --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ../../protos/metadata/vinyl.proto



echo changing some imports...
sed -i 's/import store_pb2 as store__pb2/import logic.protogen.store_pb2 as store__pb2/g' ./src/logic/protogen/store_pb2_grpc.py
sed -i 's/import subscription_pb2 as subscription__pb2/import logic.protogen.subscription_pb2 as subscription__pb2/g' ./src/logic/protogen/subscription_pb2_grpc.py
sed -i 's/import customer_pb2 as customer__pb2/import logic.protogen.customer_pb2 as customer__pb2/g' ./src/logic/protogen/customer_pb2_grpc.py
sed -i 's/import book_pb2 as book__pb2/import logic.protogen.book_pb2 as book__pb2/g' ./src/logic/protogen/book_pb2_grpc.py
sed -i 's/import song_pb2 as song__pb2/import logic.protogen.song_pb2 as song__pb2/g' ./src/logic/protogen/song_pb2_grpc.py
sed -i 's/import vinyl_pb2 as vinyl__pb2/import logic.protogen.vinyl_pb2 as vinyl__pb2/g' ./src/logic/protogen/vinyl_pb2_grpc.py

echo Ok