import zmq
import keyboard

c = zmq.Context()
s = c.socket(zmq.PULL) # Socket type PULL
s.connect("tcp://127.0.0.1:7000") # Binding it to port 7000 and tcp address 127.0.0.1 
print("Connection Established ")
while True:
    job = s.recv_json()  # Recieve Taska from server
    print ("Received job no. : ",job)
    
