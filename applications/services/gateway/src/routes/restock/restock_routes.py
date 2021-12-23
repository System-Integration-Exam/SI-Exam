from clients.reservation import restock_client
from flask import request, current_app


def create_restock():
    try:
        return restock_client.make_restock_request(request.json)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def collect_routes(app):
    app.add_url_rule("/restock", view_func=create_restock, methods=["POST"])
