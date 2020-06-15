# time_series_grpc_client
Client side of the gRPC time series assignment.

This client was created with the packages grpcio and grpcio-tools. The proto file was defined in the first place, set in both server and client and then the generation of the protocol buffer files was done by the compiler based on this proto file.

The project is divided in a modular fashion. The files necessary to run the gRPC stub are located in the grpc_stub folder. In the flask_app folder, all files to run a Flask app are located. This folder also contains the html template file which will act as frontend. Finally, there is a tests folder.

The client app has been created with an OOP approach, definining an actor for each necessary action. This enables readability, maintainability and extensibility. All the actors can be easily modified or extended with new functions if new requirements were to arise. Note that for such a simple example, this approach might seem like overdoing, yet it has been chosen for the sake of presentability.

I have decided to go for a very simple Flask application that would redirect the HTTP calls from a browser to the python functions that will trigger the entire gRPC communication process. The html page is a very simple template in which a clickable button will redirect to the URL that makes the HTTP GET call, triggering the python function that will start the entire gRPC process, finally answering the JSON, which will be shown in the browser.

# How to run the client
Clone the repository and, in your virtual environment's terminal, run:

```pip install -r requirements```

Run the ```__main__.py``` file located in the root directory. Your Flask app is running and ready to receive calls in the default local port 5000.

At the moment, it is not possible to specify the gRPC port since the html template makes a fixed call. It would be possible to modify this by, for example, adding some query parameters in the HTTP call.

# How to start the gRPC process
Make sure you have set up the gRPC server properly (https://github.com/jvbustelo/time_series_grpc_server).

Once the Flask app is running, navigate with your browser to http://localhost:5000/. When clicking in the link, the process will start and you will eventually see in the screen the raw JSON.
