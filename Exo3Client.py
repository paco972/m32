#!/usr/bin/env python3
import socket

HOST = "127.0.0.1"  # Server interface address
PORT = 65432  # Port to connect on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket: 
    serverSocket.connect((HOST, PORT)) 
    while True:
        message = bytes(input('Message : '), 'utf-8')
        serverSocket.sendall(message)            
        response = serverSocket.recv(1024).decode()
        if 'fini' in response:
            break
        print(response)
