import random

from photobox_backend_grpc.photobox_service_pb2 import CaptureResponse
from photobox_backend_grpc.photobox_service_pb2_grpc import PhotoboxControlServicer


class PhotoboxService(PhotoboxControlServicer):
    def Capture(self, request, context):
        print("Capture")
        return CaptureResponse(
            success=random.choice([True, False])
        )
