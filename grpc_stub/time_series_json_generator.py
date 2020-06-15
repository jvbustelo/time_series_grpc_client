import json

from grpc_stub.generated import time_series_pb2


class TimeSeriesJSONGenerator:

    @staticmethod
    def generate_json(time_series: time_series_pb2.TimeSeriesReply) -> str:
        """
        Create a JSON out of the time series in gRPC-object format.
        :param time_series:
        :return:
        """
        response_object = {
            'time_series': []
        }
        for point in time_series.data_points:
            response_object['time_series'].append({
                'time': point.time,
                'meterusage': point.meterusage
            })
        return json.dumps(response_object)
