import json as JSON
from logic.protogen import reservation_pb2_grpc
from logic.protogen import reservation_pb2
from utils.config import CONFIG
from google.protobuf.json_format import MessageToJson
from entities.link import Link

import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["reservation"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return reservation_pb2_grpc.ReservationGrpcStub(channel)


def create_reservation(new_reservation_json):
    response = _create_stub().CreateReservation(
        reservation_pb2.CreateRequest(
            item_id=new_reservation_json["item_id"],
            user_id=new_reservation_json["user_id"],
            store_id=new_reservation_json["store_id"],
        )
    )

    return _reservation_response_json(response)


def cancel_reservation(id):
    response = _create_stub().CancelReservation(reservation_pb2.ChangeRequest(id=id))
    return _reservation_response_json(response)


def complete_reservation(id):
    response = _create_stub().CompleteReservation(reservation_pb2.ChangeRequest(id=id))
    return _reservation_response_json(response)


def _reservation_response_json(response):
    return JSON.dumps(
        {
            "id": response.id,
            "item_id": response.item_id,
            "user_id": response.user_id,
            "status": response.status,
            "store_id": response.store_id,
        }
    )


def retrieve_users_reservation(user_id):
    response = _create_stub().RetriveUsersReservations(
        reservation_pb2.RetriveRequest(user_id=user_id)
    )

    return JSON.dumps(
        [
            {
                "payload": {
                    "id": reservation.id,
                    "item_id": reservation.item_id,
                    "user_id": reservation.user_id,
                    "status": reservation.status,
                    "store_id": reservation.store_id  
                },
                "links": [
                    Link("this user", f"/user/{reservation.user_id}").__dict__,
                    Link("this store", f"/store/{reservation.store_id}").__dict__
                ],
            }
            for reservation in response.reservations
        ]
    )
