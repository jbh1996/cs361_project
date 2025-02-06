import zmq
import time
import json
from datetime import datetime


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")
while True:
    message = socket.recv_string()
    csv_lines = json.loads(message)
    csv_string = "Name,Sponsorship Level, Checked-in?, Check-in Time\n"
    for line in csv_lines:
        append_string = ""
        counter = 0
        while counter < len(line) -1:
            append_string += str(line[counter])
            append_string += ","
            counter += 1
        if line[counter]:
            timestamp = float(line[counter])
            datetime = datetime.fromtimestamp(timestamp)
            append_string += str(datetime)
        else:
            append_string += str(line[counter])
        append_string += "\n"
        csv_string += append_string
    time.sleep(0.05)
    socket.send_string(csv_string)


