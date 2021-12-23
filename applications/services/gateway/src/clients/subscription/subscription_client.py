import json as JSON
from logic.protogen import subscription_pb2_grpc
from logic.protogen import subscription_pb2
from utils.config import CONFIG
from google.protobuf.json_format import MessageToJson
from entities.link import Link


import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["subscription"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return subscription_pb2_grpc.SubscriptionStub(channel)


def create_subscription(new_subscription_json):
    return (
        _create_stub()
        .CreateSubscription(
            subscription_pb2.CreateSubscriptionRequest(
                is_active=new_subscription_json["is_active"],
                expiration_date=new_subscription_json["expiration_date"],
            )
        )
        .msg
    )


def read_subscription(subscription_id):
    response = _create_stub().ReadSubscription(
        subscription_pb2.ReadSubscriptionRequest(id=subscription_id)
    )
    return {
        "payload": {
            "is_active": response.is_active,
            "expiration_date": response.expiration_date,
            "created_at": response.created_at,
            "updated_at": response.updated_at,
        },
        "links": [
            Link("this subscription", f"/subscription/{response.id}"),
            Link("all subscriptions", "/subscription"),
        ],
    }


def read_subscription_list():
    response = _create_stub().ReadSubscriptionList(
        subscription_pb2.ReadSubscriptionListRequest()
    )
    subscriptions = []
    for sub in response.subscription_list:
        obj = {
            "payload": {
                "id": sub.id,
                "is_active": sub.is_active,
                "expiration_date": sub.expiration_date,
                "created_at": sub.created_at,
                "updated_at": sub.updated_at,
            },
            "links": [
                Link("this subscription", f"/subscription/{sub.id}").__dict__,
                Link("all subscriptions", "/subscription").__dict__,
            ],
        }
        subscriptions.append(obj)

    return JSON.dumps(subscriptions)


def update_subscription(update_subscription_json, id):
    return (
        _create_stub()
        .UpdateSubscription(
            subscription_pb2.UpdateSubscriptionRequest(
                id=id,
                is_active=update_subscription_json["is_active"],
                expiration_date=update_subscription_json["expiration_date"],
            )
        )
        .msg
    )


def delete_subscription(subscription_id):
    response = _create_stub().DeleteSubscription(
        subscription_pb2.DeleteSubscriptionRequest(id=subscription_id)
    )
    return MessageToJson(response)
