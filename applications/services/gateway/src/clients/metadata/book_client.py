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
    response = _create_stub().getBookById(book_pb2.GetBookByIdRequest(id=book_id))
    return {
        "payload": {
            "title": response.title,
            "author": response.author,
            "rating": response.rating,
        },
        "links": [Link("this book", f"/book/{response.id}"), Link("all books", "/book")],
    }


def read_book_list():
    response = _create_stub().getAllBooks(book_pb2.GetAllBooksRequest())
    books = [
        {
            "payload": {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "rating": book.rating,
            },
            "links": [
                Link("this book", f"/book/{book.id}").__dict__,
                Link("all books", "/book").__dict__,
            ],
        }
        for book in response.books
    ]
    return JSON.dumps(books)


def update_book(update_book_json, id):
    return (
        _create_stub()
        .updateBook(
            book_pb2.UpdateBookRequest(
                id=id,
                title=update_book_json["title"],
                author=update_book_json["author"],
                rating=update_book_json["rating"],
            )
        )
        .statusMessage
    )


def delete_book(book_id):
    response = _create_stub().deleteBookById(book_pb2.DeleteBookByIdRequest(id=book_id))
    return MessageToJson(response)
