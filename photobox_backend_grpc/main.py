from concurrent import futures

import grpc

from photobox_backend_grpc import photobox_service_pb2_grpc
from photobox_backend_grpc.photobox_servicer import PhotoboxService


def runserver():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    interface = '[::]:50051'
    photobox_service_pb2_grpc.add_PhotoboxControlServicer_to_server(PhotoboxService(), server)
    server.add_insecure_port(interface)
    server.start()

    print("Server started on {}".format(interface))

    server.wait_for_termination()


if __name__ == '__main__':
    runserver()
