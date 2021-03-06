from clients.reservation import reservation_client
from flask import request, current_app
from grpc import RpcError


def create_reservation():
    try:
        return reservation_client.create_reservation(request.json), 201
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def cancel_reservation():
    try:
        return reservation_client.cancel_reservation(request.json["id"])
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def complete_reservation():
    try:
        return reservation_client.complete_reservation(request.json["id"])
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def retrieve_users_reservation(userId):
    try:
        return reservation_client.retrieve_users_reservation(userId)
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def collect_routes(app):
    app.add_url_rule("/reservation/create", view_func=create_reservation, methods=["POST"])
    app.add_url_rule(
        "/reservation/cancel", view_func=cancel_reservation, methods=["POST"]
    )
    app.add_url_rule(
        "/reservation/complete", view_func=complete_reservation, methods=["POST"]
    )
    app.add_url_rule(
        "/reservation/<string:userId>", view_func=retrieve_users_reservation, methods=["GET"]
    )
