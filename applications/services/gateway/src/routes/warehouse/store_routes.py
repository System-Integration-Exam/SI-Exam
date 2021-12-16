from clients import warehouse_routes
from flask import request


def create_store():
    try:
        return warehouse_routes.create_store(request.json)
    except Exception as e:
        print(e)
        return "500"


def read_store(id):
    try:
        return warehouse_routes.read_store(id)
    except Exception as e:
        print(e)
        return "500"


def update_store(id):
    try:
        return warehouse_routes.update_store(id, request.json)
    except Exception as e:
        print(e)
        return "500"


def delete_store(id):
    try:
        return warehouse_routes.delete_store(id)
    except Exception as e:
        print(e)
        return "500"


def read_store_list():
    try:
        return warehouse_routes.read_store_list()
    except Exception as e:
        print(e)
        return "500"


def add_book_to_store(store_id, book_id):
    try:
        return warehouse_routes.add_book_to_store(store_id, book_id)
    except Exception as e:
        print(e)
        return "500"


def remove_book_from_store(store_id, book_id):
    try:
        return warehouse_routes.remove_book_from_store(store_id, book_id)
    except Exception as e:
        print(e)
        return "500"


def get_amount_of_specific_book_from_store(store_id, book_id):
    try:
        return warehouse_routes.get_amount_of_specific_book_from_store(
            store_id, book_id
        )
    except Exception as e:
        print(e)
        return "500"


def add_vinyl_to_store(store_id, vinyl_id):
    try:
        return warehouse_routes.add_vinyl_to_store(store_id, vinyl_id)
    except Exception as e:
        print(e)
        return "500"


def remove_vinyl_from_store(store_id, vinyl_id):
    try:
        return warehouse_routes.remove_vinyl_from_store(store_id, vinyl_id)
    except Exception as e:
        print(e)
        return "500"


def get_amount_of_specific_vinyl_from_store(store_id, vinyl_id):
    try:
        return warehouse_routes.get_amount_of_specific_vinyl_from_store(
            store_id, vinyl_id
        )
    except Exception as e:
        print(e)
        return "500"


def return_item_stock_info(uuid, store_id):
    try:
        return warehouse_routes.return_item_stock_info(uuid, store_id)
    except Exception as e:
        print(e)
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
        "/store/total=<int:store_id>&<int:book_id>",
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
        "/store/total=<int:store_id>&<int:vinyl_id>",
        view_func=get_amount_of_specific_vinyl_from_store,
        methods=["GET"],
    )
    app.add_url_rule(
        "/store/return=<string:uuid>&<int:store_id>",
        view_func=return_item_stock_info,
        methods=["GET"],
    )