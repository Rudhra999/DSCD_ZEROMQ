import zmq     #ZeroMQ library 
import time
import keyboard 

con = zmq.Context()
s = con.socket(zmq.PUSH)  # Socket type PUSH
s.bind("tcp://127.0.0.1:7000") # Binding it to port 7000 and tcp address 127.0.0.1 
print("Connection Establihed ")

Tasks=int(input("Enter how many Takss u want to give out "))  # User will define how many tasks he wanna send out to the workers
print("Press p to start giving out Tasks ")
while True:                                   # Infinite loop is used to wait for user to press p.
    if  keyboard.read_key()== "p":            # If User press "P" , Tasks will be given out
        for num in range(Tasks):
            s.send_json(num)                  # Sending the Tasks 
            time.sleep(0.5)
        print("Tasks are Done ")
        break