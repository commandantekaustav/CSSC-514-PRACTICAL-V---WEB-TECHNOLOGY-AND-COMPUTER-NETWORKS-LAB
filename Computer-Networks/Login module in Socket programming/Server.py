import socket
import os
import threading
import hashlib

IP="192.168.43.43"
PORT=8080
dns_table ={"www.google.com":"192.168.1.1",
            "www.amazon.com":"192.168.1.2",
            "www.facebook.com":"192.168.1.3",
            "www.twitter.com":"192.168.1.4"}
# Create Socket (TCP) Connection
ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) 
ThreadCount = 0
try:
    ServerSocket.bind((IP, PORT))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)

# Function : For each client 
def threaded_client(connection):
    connection.send(str.encode('Enter Domain Name : ')) # Request Username
    req_domain = connection.recv(2048)
    connection.send(str.encode('ENTER IP : ')) # Request Password
    req_ip = connection.recv(2048)
    req_ip = req_ip.decode()
    req_domain = req_domain.decode()
    if(dns_table[req_domain] == req_ip):
            connection.send(str.encode('Connection Successful')) # Response Code for Connected Client 
            print('Connected : ',req_domain)
    else:
            connection.send(str.encode('Login Failed')) # Response code for login failed
            print('Connection denied : ',req_domain)
    while True:
        break
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    client_handler = threading.Thread(
        target=threaded_client,
        args=(Client,)  
    )
    client_handler.start()
    ThreadCount += 1
    print('Connection Request: ' + str(ThreadCount))
ServerSocket.close()
