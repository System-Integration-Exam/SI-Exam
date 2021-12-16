#!/bin/bash

# Cleanup
echo removing older protogen...
rm -rf ./protogen
mkdir ./protogen

# Protogen
echo generating protogen...
python -m grpc_tools.protoc -I../../protos/metadata --python_out=./protogen --grpc_python_out=./protogen ../../protos/metadata/book.proto
python -m grpc_tools.protoc -I../../protos/metadata --python_out=./protogen --grpc_python_out=./protogen ../../protos/metadata/vinyl.proto
python -m grpc_tools.protoc -I../../protos/metadata --python_out=./protogen --grpc_python_out=./protogen ../../protos/metadata/song.proto

echo changing some imports...
sed -i 's/import book_pb2 as book__pb2/import protogen.book_pb2 as book__pb2/g' ./protogen/book_pb2_grpc.py
sed -i 's/import song_pb2 as song__pb2/import protogen.song_pb2 as song__pb2/g' ./protogen/song_pb2_grpc.py
sed -i 's/import vinyl_pb2 as vinyl__pb2/import protogen.vinyl_pb2 as vinyl__pb2/g' ./protogen/vinyl_pb2_grpc.py

echo Ok