
    
import time, socket, sys
 

host = socket.gethostname() 
port = 8080 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

name = input('Enter Friend\'s name: ')
 
 

 
client_socket.send(name.encode())
server_name = client_socket.recv(1024)
server_name = server_name.decode()
 
print(server_name,' has joined...')
while True:
    message = (client_socket.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    client_socket.send(message.encode())
    if(message=='bye'):
        break
