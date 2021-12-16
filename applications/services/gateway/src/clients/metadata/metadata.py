import json as JSON
from logic.protogen.metadata_protogen import book_pb2_grpc
from logic.protogen.metadata_protogen import book_pb2
from logic.protogen.metadata_protogen import song_pb2_grpc
from logic.protogen.metadata_protogen import song_pb2
from logic.protogen.metadata_protogen import vinyl_pb2_grpc
from logic.protogen.metadata_protogen import vinyl_pb2
from utils.config import CONFIG
from entities.warehouse.store import Store

import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["warehouse"]


# creating stubs for each proto file
def _createBookStub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return book_pb2_grpc.BookStub(channel)
    
def _createSongStub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return song_pb2_grpc.SongStub(channel)
    
def _createvinylStub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return vinyl_pb2_grpc.VinylStub(channel)


# book client
def createBook(json):
    return (
        _createBookStub()
        .createBook(
            book_pb2.CreateBookRequest(
                title=json["title"],
                author=json["author"],
                rating=json["rating"]
            )
        )
        .msg
    )

def getBookById(json):
    return (
        _createBookStub()
        .createBook(
            book_pb2.CreateBookRequest(
                id=json["id"]
            )
        )
        .msg
    )

def updateBook(json):
    return (
        _createBookStub()
        .createBook(
            book_pb2.CreateBookRequest(
                id=json["id"],
                title=json["title"],
                author=json["author"],
                rating=json["rating"]
            )
        )
        .msg
    )

def deleteBookById(json):
    return (
        _createBookStub()
        .createBook(
            book_pb2.CreateBookRequest(
                id=json["id"]
            )
        )
        .msg
    )

def getAllBooks():
    return (
        _createBookStub()
        .createBook(
            book_pb2.CreateBookRequest(
            )
        )
        .msg
    )


