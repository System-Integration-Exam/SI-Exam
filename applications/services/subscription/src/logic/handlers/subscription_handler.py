from connection.sqlite_connection import execute_query, fetch_one, fetch_all
from logic.protogen import subscription_pb2


def create_subscription(
    request: subscription_pb2.CreateSubscriptionRequest,
) -> subscription_pb2.CreateSubscriptionResponse:
    try:
        execute_query(
            f"""
                      INSERT INTO subscription(is_active, expiration_date)
                      VALUES ('{request.is_active}','{request.expiration_date}')
                      """
        )
        return subscription_pb2.CreateSubscriptionResponse(msg="Ok")
    except Exception as e:
        print(e)
        return subscription_pb2.CreateSubscriptionResponse(
            msg="Err: Could not execute query"
        )


def read_subscription(
    request: subscription_pb2.ReadSubscriptionRequest,
) -> subscription_pb2.ReadSubscriptionResponse:
    try:
        res = fetch_one(
            f"""
                SELECT *
                FROM subscription
                WHERE id = {int(request.id)}
                      """
        )
        return subscription_pb2.ReadSubscriptionResponse(
            id=res[0],
            is_active=bool(res[1]),
            expiration_date=res[2],
            created_at=res[3],
            updated_at=res[4],
        )
    except Exception as e:
        print(e)
        return subscription_pb2.ReadSubscriptionResponse(
            subscription_pb2.ReadSubscriptionResponse(
                id=-1,
                is_active="",
                expiration_date="",
                created_at="",
                updated_at="",
            )
        )


def read_subscription_list(
    request: subscription_pb2.ReadSubscriptionListRequest,
) -> subscription_pb2.ReadSubscriptionListResponse:
    try:
        res = fetch_all("SELECT * FROM subscription")
        subscription_objects = []
        for subscription in res:
            subscrip = subscription_pb2.ReadSubscriptionListResponse.SubscriptionObject(
                id=subscription[0],
                is_active=bool(subscription[1]),
                expiration_date=subscription[2],
                created_at=subscription[3],
                updated_at=subscription[4],
            )
            subscription_objects.append(subscrip)

        return subscription_pb2.ReadSubscriptionListResponse(
            subscription_list=subscription_objects
        )
    except Exception as e:
        print(e)
        return subscription_pb2.ReadSubscriptionListResponse(subscription_list=[])


def update_subscription(
    request: subscription_pb2.UpdateSubscriptionRequest,
) -> subscription_pb2.UpdateSubscriptionResponse:
    try:
        execute_query(
            f"""
                      UPDATE subscription
                      SET (is_active, expiration_date) = ('{request.is_active}','{request.expiration_date}')
                      WHERE id = {int(request.id)}
                      """
        )
        return subscription_pb2.UpdateSubscriptionResponse(msg="Ok")
    except Exception as e:
        print(e)
        return subscription_pb2.UpdateSubscriptionResponse(
            msg="Err: Could not execute query"
        )


def delete_subscription(
    request: subscription_pb2.DeleteSubscriptionRequest,
) -> subscription_pb2.DeleteSubscriptionResponse:
    try:
        execute_query(
            f"""
                      DELETE FROM subscription
                      WHERE id = {int(request.id)}
                      """
        )
        return subscription_pb2.DeleteSubscriptionResponse(msg="subscription deleted")
    except Exception as e:
        print(e)
        return subscription_pb2.DeleteSubscriptionResponse(
            msg="Err: an error occurred. please try again"
        )
