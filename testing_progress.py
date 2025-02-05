context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.bind("tcp://localhost:5555")