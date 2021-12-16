from clients.subscription import customer_client
from flask import request


def create_customer():
    try:
        return customer_client.create_customer(request.json)
    except Exception as e:
        print(e)
        return "500"


def read_customer(id):
    try:
        return customer_client.read_customer(id)
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def read_customer_list():
    try:
        return customer_client.read_customer_list()
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def update_customer(id):
    try:
        return customer_client.update_customer(request.json, id)
    except Exception as e:
        print(e)
        return "500"


def delete_customer(id):
    try:
        return customer_client.delete_customer(id)
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def collect_routes(app):
    app.add_url_rule("/customer", view_func=create_customer, methods=["POST"])
    app.add_url_rule("/customer/<int:id>", view_func=read_customer, methods=["GET"])
    app.add_url_rule("/customer", view_func=read_customer_list, methods=["GET"])
    app.add_url_rule("/customer/<int:id>", view_func=update_customer, methods=["PUT"])
    app.add_url_rule(
        "/customer/<int:id>", view_func=delete_customer, methods=["DELETE"]
    )
