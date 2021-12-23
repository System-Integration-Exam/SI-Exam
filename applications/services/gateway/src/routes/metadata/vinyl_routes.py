from clients.metadata import vinyl_client
from flask import request, current_app


def create_vinyl():
    try:
        return vinyl_client.create_vinyl(request.json)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def read_vinyl(id):
    try:
        return vinyl_client.read_vinyl(id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def read_vinyl_list():
    try:
        return vinyl_client.read_vinyl_list()
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def update_vinyl(id):
    try:
        return vinyl_client.update_vinyl(request.json, id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def delete_vinyl(id):
    try:
        return vinyl_client.delete_vinyl(id)
    except Exception as e:
        current_app.logger.error("%s", e)
        return "500"


def collect_routes(app):
    app.add_url_rule("/vinyl", view_func=create_vinyl, methods=["POST"])
    app.add_url_rule("/vinyl/<string:id>", view_func=read_vinyl, methods=["GET"])
    app.add_url_rule("/vinyl", view_func=read_vinyl_list, methods=["GET"])
    app.add_url_rule("/vinyl/<string:id>", view_func=update_vinyl, methods=["PUT"])
    app.add_url_rule("/vinyl/<string:id>", view_func=delete_vinyl, methods=["DELETE"])
