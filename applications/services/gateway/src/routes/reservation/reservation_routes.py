from clients.reservation import reservation_client
from flask import request


def create_reservation():
    try:
        return reservation_client.create_reservation(request.json)
    except Exception as e:
        print(e)
        return "500"


def cancel_reservation():
    try:
        return reservation_client.cancel_reservation(request.json["id"])
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def complete_reservation():
    try:
        return reservation_client.complete_reservation(request.json["id"])
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def retrieve_users_reservation(userId):
    try:
        return reservation_client.retrieve_users_reservation(userId)
    except Exception as e:
        print(e)
        return "500"


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
