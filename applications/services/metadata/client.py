import grpc

# import the generated classes
import protogen.book_pb2 as book_pb2
import protogen.book_pb2_grpc as book_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = book_pb2_grpc.BookStub(channel)

# create a valid request message
id = book_pb2.BookRequest(id=10)

# make the call
response = stub.getBookInfo(id)

# et voilà
print(response.id)