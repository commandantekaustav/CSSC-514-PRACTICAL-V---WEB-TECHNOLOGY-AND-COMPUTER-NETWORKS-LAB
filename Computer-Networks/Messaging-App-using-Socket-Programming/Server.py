

import time, socket, sys
 
#new_socket = socket.socket()
host = socket.gethostname() 
port = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port)) 
server_socket.listen(5) 
host_name = socket.gethostname()

 
name = input('Enter name: ')
 
#server_socket.listen(1) 
 
 
conn, add = server_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
 
conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
    if(message=='bye'):
        break



    
