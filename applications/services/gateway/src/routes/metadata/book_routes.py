from clients.metadata import book_client
from flask import request, current_app


def create_book():
    try:
        return book_client.create_book(request.json), 201
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def read_book(id):
    try:
        return book_client.read_book(id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def read_book_list():
    try:
        return book_client.read_book_list()
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def update_book(id):
    try:
        return book_client.update_book(request.json, id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def delete_book(id):
    try:
        return book_client.delete_book(id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def collect_routes(app):
    app.add_url_rule("/book", view_func=create_book, methods=["POST"])
    app.add_url_rule("/book/<string:id>", view_func=read_book, methods=["GET"])
    app.add_url_rule("/book", view_func=read_book_list, methods=["GET"])
    app.add_url_rule("/book/<string:id>", view_func=update_book, methods=["PUT"])
    app.add_url_rule("/book/<string:id>", view_func=delete_book, methods=["DELETE"])
