from flask import Flask, render_template

from grpc_stub.time_series_client import request_time_series
from grpc_stub.time_series_json_generator import TimeSeriesJSONGenerator

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the html template for the main page
    :return:
    """
    return render_template('frontend_template.html')


@app.route('/get_time_series_json')
def get_time_series_json():
    """
    Make proto request of the time series from the gRPC server and turn it into a JSON object to show in the frontend.
    :return:
    """
    time_series = request_time_series()
    json_response = TimeSeriesJSONGenerator.generate_json(time_series)
    return json_response
