import zmq
import time
import keyboard
print("Press d for Default Port , Press any key for manually entring port no.")
print("Press p for quitting programe")

if keyboard.read_key()== "d":
    p=7000     #Default Port
else:
    p=int(input("Enter the Port No. : "))# Enter your Port no. here

c = zmq.Context()
s = c.socket(zmq.PAIR)     # Socket Type 
s.bind('tcp://127.0.0.1:%s'% p)     # Binding to given port and localhost
print("Connection Established , Port : %s"%p)

while True:
    i=input("Server wrote : ")  # Taking Input from Server
    s.send_json(i)    # Sending Client Message to Server 
    c= s.recv_json() # Recieving form Client
    print("Client sent :",c)
    time.sleep(1)
    if keyboard.read_key()== "p": # To exist the Program
        break