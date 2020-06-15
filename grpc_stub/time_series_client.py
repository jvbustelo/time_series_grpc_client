import grpc

from grpc_stub.generated import time_series_pb2
from grpc_stub.generated import time_series_pb2_grpc


def request_time_series(port: int = 50051) -> time_series_pb2.TimeSeriesReply:
    """
    gRPC stub that will request the time series to the gRPC server.
    :param port: port number in which the gRPC server is exposed
    :return:
    """
    with grpc.insecure_channel('localhost:{}'.format(str(port))) as channel:
        stub = time_series_pb2_grpc.TimeSeriesStub(channel)
        response = stub.Reply(time_series_pb2.TimeSeriesRequest())
    return response
