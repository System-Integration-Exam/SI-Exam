from clients import warehouse
from flask import request, current_app
from entities import link

def create_store():
    try:
        return warehouse.create_store(request.json)

    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def read_store(id):
    try:
        return warehouse.read_store(id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def update_store(id):
    try:
        return warehouse.update_store(id, request.json)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def delete_store(id):
    try:
        return warehouse.delete_store(id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def read_store_list():
    try:
        return warehouse.read_store_list()
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def add_book_to_store(store_id, book_id):
    try:
        return warehouse.add_book_to_store(store_id, book_id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def remove_book_from_store(store_id, book_id):
    try:
        return warehouse.remove_book_from_store(store_id, book_id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def get_amount_of_specific_book_from_store(store_id, book_id):
    try:
        return warehouse.get_amount_of_specific_book_from_store(store_id, book_id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def add_vinyl_to_store(store_id, vinyl_id):
    try:
        return warehouse.add_vinyl_to_store(store_id, vinyl_id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def remove_vinyl_from_store(store_id, vinyl_id):
    try:
        return warehouse.remove_vinyl_from_store(store_id, vinyl_id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def get_amount_of_specific_vinyl_from_store(store_id, vinyl_id):
    try:
        return warehouse.get_amount_of_specific_vinyl_from_store(store_id, vinyl_id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def return_item_stock_info(uuid, store_id):
    try:
        return warehouse.return_item_stock_info(uuid, store_id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def collect_routes(app):
    
    app.add_url_rule("/store", view_func=create_store, methods=["POST"])
    app.add_url_rule("/store/<int:id>", view_func=read_store, methods=["GET"])
    app.add_url_rule("/store/<int:id>", view_func=update_store, methods=["PUT"])
    app.add_url_rule("/store/<int:id>", view_func=delete_store, methods=["DELETE"])
    app.add_url_rule("/store", view_func=read_store_list, methods=["GET"])
    app.add_url_rule(
        "/store/add-book=<int:store_id>&<int:book_id>",
        view_func=add_book_to_store,
        methods=["POST"],
    )
    app.add_url_rule(
        "/store/remove-book=<int:store_id>&<int:book_id>",
        view_func=remove_book_from_store,
        methods=["DELETE"],
    )
    app.add_url_rule(
        "/store/total-book=<int:store_id>&<int:book_id>",
        view_func=get_amount_of_specific_book_from_store,
        methods=["GET"],
    )
    app.add_url_rule("/store", view_func=read_store_list, methods=["GET"])
    app.add_url_rule(
        "/store/add-vinyl=<int:store_id>&<int:vinyl_id>",
        view_func=add_vinyl_to_store,
        methods=["POST"],
    )
    app.add_url_rule(
        "/store/remove-vinyl=<int:store_id>&<int:vinyl_id>",
        view_func=remove_vinyl_from_store,
        methods=["DELETE"],
    )
    app.add_url_rule(
        "/store/total-vinyl=<int:store_id>&<int:vinyl_id>",
        view_func=get_amount_of_specific_vinyl_from_store,
        methods=["GET"],
    )
    app.add_url_rule(
        "/store/return=<string:uuid>&<int:store_id>",
        view_func=return_item_stock_info,
        methods=["GET"],
    )
