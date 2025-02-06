import zmq
import time
import json


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    message = socket.recv_string()
    data_dict = json.loads(message)
    window = time.time() - data_dict["window"]
    response_array = []
    for entry in data_dict["array"]:
        if len(entry) == 3:
            if entry[2] > window:
                response_array.append([entry[0], entry[1]])
    response_string = json.dumps(response_array)
    socket.send_string(response_string)