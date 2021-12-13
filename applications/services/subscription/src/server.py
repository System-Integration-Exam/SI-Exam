import utils.config
import futures

URL = f"{config["host"]}:{config["port"]}"
MAX_WORKERS = config["max_workers"]

def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(MAX_WORKERS))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port(MAX_WORKERS)
    server.start()
    server.wait_for_termination()
  
if __name__ == "__main__":
    serve()