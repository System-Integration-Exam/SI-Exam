from clients.reservation import restock_client
from flask import request, current_app
from grpc import RpcError


def create_restock():
    try:
        restock_client.make_restock_request(request.json)
        return '', 202
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def collect_routes(app):
    app.add_url_rule("/restock", view_func=create_restock, methods=["POST"])
