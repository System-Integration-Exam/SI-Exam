from logic.protogen.subscription_pb2_grpc import SubscriptionServicer
from logic.handlers import subscription_handler


class SubscriptionRouter(SubscriptionServicer):
    def CreateSubscription(self, request, _) -> None:
        return subscription_handler.create_subscription(request)

    def ReadSubscriptionList(self, request, _) -> None:
        return subscription_handler.read_subscription_list(request)

    def ReadSubscription(self, request, _) -> None:
        return subscription_handler.read_subscription(request)

    def UpdateSubscription(self, request, _) -> None:
        return subscription_handler.update_subscription(request)

    def DeleteSubscription(self, request, _) -> None:
        return subscription_handler.delete_subscription(request)
