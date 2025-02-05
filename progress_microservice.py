import zmq
import time
import json


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_string()
    print(message)
    working_array = message.split(",")
    response_dict = {}
    total_dict = {}
    for entry in working_array:
        entry_array = entry.split(";")
        if len(entry_array) != 2:
            continue
        if entry_array[1] == "True":
            if entry_array[0] in response_dict:
                response_dict[entry_array[0]] += 100
            else:
                response_dict[entry_array[0]] = 100
    for entry in working_array:
        entry_array = entry.split(";")
        if len(entry_array) != 2:
            continue
        if entry_array[0] in total_dict:
            total_dict[entry_array[0]] += 1
        else:
            total_dict[entry_array[0]] = 1
    for key in response_dict:
        response_dict[key] = response_dict[key] / total_dict[key]
    time.sleep(0.1)
    socket.send_string(json.dumps(response_dict))
