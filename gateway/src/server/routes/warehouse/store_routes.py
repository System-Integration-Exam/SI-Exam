
def get()
    pass





def collect_routes(app):
    app.add_url_rule("/store", view_func=home_route, methods=["GET"])
    app.add_url_rule("/store", view_func=health_check_route, methods=["POST"])
    app.add_url_rule("/store/<int:id>", view_func=health_check_route, methods=["PUT"])
    app.add_url_rule("/store/<int:id>", view_func=health_check_route, methods=["GET"])
    app.add_url_rule("/store/<int:id>", view_func=health_check_route, methods=["DELETE"])
    
