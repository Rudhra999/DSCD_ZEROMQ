import zmq
import time
import keyboard
print("1. Press d for Default Port , Press any key for manually entring port no.")
print("2. Press p for quitting programe")
if keyboard.read_key()== "d":
    p=7000  #Default Port
else:
    p=int(input("Enter the Port No. : ")) # Enter your Port no. here

c = zmq.Context()
s = c.socket(zmq.PAIR)      # Socket Type
s.connect("tcp://127.0.0.1:%s"%p)       # Binding to given port and localhost
print("Connection Established , Port : %s"%p)
while True:
    server_ni_bheja = s.recv_json()  # Recieving form server
    print("Server Sent",server_ni_bheja)
    i=input("Client wrote : ")         # Taking Input from Client 
    s.send_json(i)        # Sending Client Message to Server
    time.sleep(1)
    if keyboard.read_key()== "p":
        break