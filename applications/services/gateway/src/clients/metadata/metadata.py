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
    
def _createVinylStub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return vinyl_pb2_grpc.VinylStub(channel)


# book methods
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
        .getBookById(
            book_pb2.GetBookByIdRequest(
                id=json["id"]
            )
        )
        .msg
    )

def updateBook(json):
    return (
        _createBookStub()
        .updateBook(
            book_pb2.UpdateBookRequest(
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
        .deleteBookById(
            book_pb2.DeleteBookByIdRequest(
                id=json["id"]
            )
        )
        .msg
    )

def getAllBooks():
    return (
        _createBookStub()
        .getAllBooks(
            book_pb2.GetAllBooksRequest()
        )
        .msg
    )


# song methods
def createSong(json):
    return (
        _createSongStub()
        .createSong(
            song_pb2.CreateSongRequest(
                title=json["title"],
                duration_sec=json["duration_sec"],
                vinyl_id=json["vinyl_id"]
            )
        )
        .msg
    )

def getSongById(json):
    return (
        _createSongStub()
        .getSongById(
            song_pb2.GetSongByIdRequest(
                id=json["id"]
            )
        )
        .msg
    )

def updateSong(json):
    return (
        _createSongStub()
        .updateSong(
            song_pb2.UpdateSongRequest(
                id=json["id"],
                title=json["title"],
                duration_sec=json["duration_sec"],
                vinyl_id=json["vinyl_id"]
            )
        )
        .msg
    )

def deleteSongById(json):
    return (
        _createSongStub()
        .deleteSongById(
            song_pb2.DeleteSongByIdRequest(
                id=json["id"]
            )
        )
        .msg
    )

def getAllSongs():
    return (
        _createSongStub()
        .getAllSongs(
            song_pb2.GetAllSongsRequest()
        )
        .msg
    )


# song methods
def createVinyl(json):
    return (
        _createVinylStub()
        .createVinyl(
            vinyl_pb2.CreateVinylRequest(
                artist=json["artist"],
                genre=json["genre"]
            )
        )
        .msg
    )

def getVinylById(json):
    return (
        _createVinylStub()
        .getVinylById(
            vinyl_pb2.GetVinylByIdRequest(
                id=json["id"]
            )
        )
        .msg
    )

def updateVinyl(json):
    return (
        _createVinylStub()
        .updateVinyl(
            vinyl_pb2.UpdateVinylRequest(
                id=json["id"],
                artist=json["artist"],
                genre=json["genre"]
            )
        )
        .msg
    )

def deleteVinylById(json):
    return (
        _createVinylStub()
        .deleteVinylById(
            vinyl_pb2.DeleteVinylByIdRequest(
                id=json["id"]
            )
        )
        .msg
    )

def getAllVinyl():
    return (
        _createVinylStub()
        .getAllVinyl(
            vinyl_pb2.GetAllVinylRequest()
        )
        .msg
    )





