import socket

dns_table={"www.google.com":"192.165.1.1",
           "www.youtube.com":"192.165.1.2",
           "www.python.com":"192.165.1.3",
           "www.amazon.com":"192.165.1.4",
           "www.gmail.com":"192.165.1.5"}

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Starting Server.....")
s.bind(("127.0.0.1", 1234))

while True:
    data, address = s.recvfrom(1024)
    print(f"{address} wants to fetch data!")
    data = data.decode()
    ip = dns_table.get(data, "Not Found!").encode()
    send = s.sendto(ip, address)

s.close()
