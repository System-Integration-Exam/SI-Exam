from logic.protogen.customer_pb2_grpc import CustomerServicer
from logic.handlers import customer_handler


class CustomerRouter(CustomerServicer):
    def CreateCustomer(self, request, _) -> None:
        return customer_handler.create_customer(request)

    def ReadCustomer(self, request, _) -> None:
        return customer_handler.read_customer(request)

    def ReadCustomerList(self, request, _) -> None:
        return customer_handler.read_customer_list(request)

    def UpdateCustomer(self, request, _) -> None:
        return customer_handler.update_customer(request)

    def DeleteCustomer(self, request, _) -> None:
        return customer_handler.delete_customer(request)
