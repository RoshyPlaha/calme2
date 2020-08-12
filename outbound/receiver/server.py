import socket
import sys

ip = '127.0.0.1'
port = 3000

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

while True:
    print("####### Server is listening #######")
    data, address = s.recvfrom(1000)
    print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")