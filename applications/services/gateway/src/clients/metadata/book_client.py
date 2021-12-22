import json as JSON
from logic.protogen import book_pb2_grpc
from logic.protogen import book_pb2
from utils.config import CONFIG
from google.protobuf.json_format import MessageToJson
from entities.link import Link


import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["metadata"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return book_pb2_grpc.BookStub(channel)


def create_book(new_book_json):
    book = (
        _create_stub().createBook(
            book_pb2.CreateBookRequest(
                title=new_book_json["title"],
                author=new_book_json["author"],
                rating=new_book_json["rating"],
            )
        )
    ).book
    return JSON.dumps(
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
        }
    )


def read_book(book_id):
    response = _create_stub().readBook(book_pb2.ReadBookRequest(id=book_id))
    return {
        "payload": {
            "title": response.title,
            "author": response.author,
            "rating": response.rating,
        },
        "links": [Link("stuff", "thing").__dict__, Link("stuff", "thing").__dict__],
    }


def read_book_list():
    response = _create_stub().readBookList(book_pb2.ReadBookListRequest())
    books = [
        {
            "payload": {
                "id": book.id,
                "title": book.subscription_id,
                "author": book.first_name,
                "rating": book.last_name,
            },
            "links": [Link("this book", f"/book/{book.id}").__dict__, Link("all books", "/book").__dict__],
        }
        for book in response.book_list
    ]
    return JSON.dumps(books)


def update_book(update_book_json, id):
    return (
        _create_stub()
        .rpdateBook(
            book_pb2.UpdateBookRequest(
                id=id,
                title=update_book_json["title"],
                author=update_book_json["author"],
                rating=update_book_json["rating"],
            )
        )
        .msg
    )


def delete_book(book_id):
    response = _create_stub().deleteBook(book_pb2.DeleteBookRequest(id=book_id))
    return MessageToJson(response)
