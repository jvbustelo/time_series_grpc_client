import json

from grpc_stub.generated import time_series_pb2
from grpc_stub.time_series_json_generator import TimeSeriesJSONGenerator


def test_json_generator():
    test_reply = time_series_pb2.TimeSeriesReply()
    test_data_point = time_series_pb2.TimeSeriesReply.DataPoint()
    test_data_point.time = '2020-01-01 00:00:00'
    test_data_point.meterusage = 1.0
    test_reply.data_points.extend([test_data_point])

    test_json = TimeSeriesJSONGenerator.generate_json(test_reply)

    assert isinstance(test_json, str)

    test_object = json.loads(test_json)

    assert len(test_object['time_series']) == 1
    assert test_object['time_series'][0]['time'] == '2020-01-01 00:00:00'
    assert test_object['time_series'][0]['meterusage'] == 1.0
