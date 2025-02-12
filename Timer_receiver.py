# server to listen for requests 
# MICROSERVICE A
import zmq
from datetime import datetime, timedelta

def convert_data(checkin_time_str, duration_str):
    """Takes the client provided check in time and duration for check window. 
    Calculates and returns elapsed time and remaining time."""
    
    current_date = datetime.now().date()
    
    # Concatenates date with check-in time, helps avoid extra calculations if check-in goes past midnight
    checkin_datetime = datetime.strptime(f"{current_date} {checkin_time_str}", '%Y-%m-%d %H:%M:%S')
    
    duration = int(duration_str)
    end_time = checkin_datetime + timedelta(minutes=duration)
    current_time = datetime.now()

    # Calculations get converted to minutes
    elapsed_time = (current_time - checkin_datetime).total_seconds() / 60
    remaining_time = (end_time - current_time).total_seconds() / 60
    
    print(f"Elapsed Time: {elapsed_time:.2f}")
    print(f"Remaining Time: {remaining_time:.2f}")
    return elapsed_time, remaining_time


def timer_program():
    """ Receives request (check-in time, duration in minutes) from client and 
    sends back elapsed and remaining time."""
    
    context = zmq.Context()                 # Required for ZeroMQ to set up env
    socket = context.socket(zmq.REP)        # Reply Socket
    socket.bind("tcp://*:5556")             # Socket will listen

    while True:
        print("Server is listening...")
        message_received = socket.recv()
        message_str = message_received.decode()
        
        checkin_time_str, duration_str = message_str.split(',')
        print(f"Message Received. Check-In Time: {checkin_time_str}, Duration: {duration_str}")
        
        # Call convert_data() to run calculations for elasped/remaining time
        elapsed_time, remaining_time = convert_data(checkin_time_str, duration_str)
        
        reply = f"Elapsed Time: {elapsed_time:.2f}, Remaining Time: {remaining_time:.2f}"
        socket.send_string(reply) 

if __name__ == "__main__":
    timer_program()
    
    

#Converting a string to a time: https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
#Converting timedelta to seconds: https://docs.python.org/3/library/datetime.html
