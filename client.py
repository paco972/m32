#!/usr/bin/env python3
import socket

HOST = "192.168.1.44"  # Server interface address
PORT = 65432  # Port to connect on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: 
    server.connect((HOST, PORT)) 
    server.sendall(b'Bonjour') 
    data = server.recv(1024) 
   
print(f"Received {data!r}")