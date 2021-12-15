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
