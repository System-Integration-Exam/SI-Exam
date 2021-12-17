from clients.restock import restock_client
from flask import request


def create_restock():
    try:
        return restock_client.create_restock(request.json)
    except Exception as e:
        print(e)
        return "500"


def collect_routes(app):
    app.add_url_rule("/restock", view_func=create_restock, methods=["POST"])