import socket


IP="192.168.43.43"
PORT=8080
# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect((IP, PORT))

c="y"
while c.upper()=="Y":
        response = client.recv(2048)
    # Input UserName
        req_domain = input(response.decode())	
        client.send(str.encode(req_domain))
        response = client.recv(2048)
        # Input Password
        req_ip = input(response.decode())	
        client.send(str.encode(req_ip))

        # Receive response 
        response = client.recv(2048)
        response = response.decode()

        print(response)
        c=input("Continue?(y/n)")
client.close()
