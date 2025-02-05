import zmq
import time


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")
while True:
    message = socket.recv_string()
    working_array = message.split(",")
    response_dict = {}
    for entry in working_array:
        entry_array = entry.split(";")
        if entry_array[1] == "True":
            if entry_array[0] in response_dict:
                response_dict[entry_array[0]] += 1
            else:
                response_dict[entry_array[0]] = 1
    time.sleep(0.1)
    socket.send_string(str(response_dict))