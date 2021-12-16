import json as JSON
from logic.protogen import customer_pb2_grpc
from logic.protogen import customer_pb2
from utils.config import CONFIG
from google.protobuf.json_format import MessageToJson


import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["subscription"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return customer_pb2_grpc.CustomerStub(channel)


def create_customer(new_customer_json):
    return (
        _create_stub()
        .CreateCustomer(
            customer_pb2.CreateCustomerRequest(
                subscription_id=new_customer_json["subscription_id"],
                first_name=new_customer_json["first_name"],
                last_name=new_customer_json["last_name"],
                email=new_customer_json["email"],
                phone_number=new_customer_json["phone_number"],
            )
        )
        .msg
    )


def read_customer(customer_id):
    response = _create_stub().ReadCustomer(
        customer_pb2.ReadCustomerRequest(id=customer_id)
    )
    return MessageToJson(response)


def read_customer_list():
    response = _create_stub().ReadCustomerList(customer_pb2.ReadCustomerListRequest())
    customers = []
    for cus in response.customer_list:
        obj = {
            "id": cus.id,
            "subscription_id": cus.subscription_id,
            "first_name": cus.first_name,
            "last_name": cus.last_name,
            "email": cus.email,
            "phone_number": cus.phone_number,
            "created_at": cus.created_at,
            "updated_at": cus.updated_at,
        }
        customers.append(obj)

    return JSON.dumps(customers)


def update_customer(update_customer_json, id):
    return (
        _create_stub()
        .UpdateCustomer(
            customer_pb2.UpdateCustomerRequest(
                id=id,
                first_name=update_customer_json["first_name"],
                last_name=update_customer_json["last_name"],
                email=update_customer_json["email"],
                phone_number=update_customer_json["phone_number"],
            )
        )
        .msg
    )


def delete_customer(customer_id):
    response = _create_stub().DeleteCustomer(
        customer_pb2.DeleteCustomerRequest(id=customer_id)
    )
    return MessageToJson(response)
