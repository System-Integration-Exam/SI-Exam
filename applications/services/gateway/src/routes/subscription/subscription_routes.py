from clients.subscription import subscription_client
from flask import request


def create_subscription():
    try:
        return subscription_client.create_subscription(request.json)
    except Exception as e:
        print(e)
        return "500"


def read_subscription(id):
    try:
        return subscription_client.read_subscription(id)
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def read_subscription_list():
    try:
        return subscription_client.read_subscription_list()
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def update_subscription(id):
    try:
        return subscription_client.update_subscription(request.json, id)
    except Exception as e:
        print(e)
        return "500"


def delete_subscription(id):
    try:
        return subscription_client.delete_subscription(id)
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def collect_routes(app):
    app.add_url_rule("/subscription", view_func=create_subscription, methods=["POST"])
    app.add_url_rule(
        "/subscription/<int:id>", view_func=read_subscription, methods=["GET"]
    )
    app.add_url_rule("/subscription", view_func=read_subscription_list, methods=["GET"])
    app.add_url_rule(
        "/subscription/<int:id>", view_func=update_subscription, methods=["PUT"]
    )
    app.add_url_rule(
        "/subscription/<int:id>", view_func=delete_subscription, methods=["DELETE"]
    )
