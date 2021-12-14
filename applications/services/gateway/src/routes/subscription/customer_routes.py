from clients.subscription import customer_client
from flask import request


def create_customer():
    try:
        return customer_client.create_customer(request.json)
    except Exception as e:
        print(e)
        return "500"
    
def read_customer(id):
    
    print("aaaaaah")
    try:
        return customer_client.read_customer(id)
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def collect_routes(app):
    app.add_url_rule("/customer", view_func=create_customer, methods=["POST"])
    app.add_url_rule("/customer/<int:id>", view_func=read_customer, methods=["GET"])