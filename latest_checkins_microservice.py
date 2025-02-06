import zmq
import time
import json


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    message = socket.recv_string()
    csv_lines = json.loads(message)