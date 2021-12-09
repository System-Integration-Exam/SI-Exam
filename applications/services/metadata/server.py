import grpc
from concurrent import futures
import time

# import the generated classes
import protogen.book_pb2 as book_pb2
import protogen.book_pb2_grpc as book_pb2_grpc

# import the original calculator.py
import entities.Book as Book
import facades.BookFacade as BF

# create a class to define the server functions, derived from
# book_pb2_grpc.BookServicer
class BookServicer(book_pb2_grpc.BookServicer):

    # calculator.getBookInfo is exposed here
    # the request and response are of the data type
    # book_pb2.Id
    def getBookInfo(self, request, context):
        response = book_pb2.BookResponse()
        book = BF.getBookInfo(request.id)

        response.id = book.id
        response.title = book.title
        response.author = book.author
        response.rating = book.rating
        
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_BookServicer_to_server`
# to add the defined class to the server
book_pb2_grpc.add_BookServicer_to_server(
        BookServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)