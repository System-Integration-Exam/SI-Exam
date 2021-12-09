# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from stubs import book_pb2 as protos_dot_book__pb2


class BookStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getBookInfo = channel.unary_unary(
                '/Book/getBookInfo',
                request_serializer=protos_dot_book__pb2.BookRequest.SerializeToString,
                response_deserializer=protos_dot_book__pb2.BookRequest.FromString,
                )


class BookServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getBookInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getBookInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getBookInfo,
                    request_deserializer=protos_dot_book__pb2.BookRequest.FromString,
                    response_serializer=protos_dot_book__pb2.BookRequest.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Book', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Book(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getBookInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Book/getBookInfo',
            protos_dot_book__pb2.BookRequest.SerializeToString,
            protos_dot_book__pb2.BookRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
