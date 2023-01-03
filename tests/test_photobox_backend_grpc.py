from photobox_backend_grpc import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_grpc_connect():
    from photobox_backend_grpc.photobox_service_pb2_grpc import PhotoboxControlStub
    from photobox_backend_grpc.photobox_service_pb2 import CaptureRequest
    from grpc import insecure_channel

    channel = insecure_channel('localhost:50051')
    stub = PhotoboxControlStub(channel)
    response = stub.Capture(CaptureRequest())
    assert response.success
