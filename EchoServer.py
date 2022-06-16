#!/usr/bin/env python3
import socket

HOST = "0.0.0.0"  # Any interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.bind((HOST, PORT))
    client.listen()
    connection, address = client.accept()
    print(f"Connected by {address}")
    with connection:
        while True:
            data = connection.recv(1024)
            if data == (b'\r\n'):
                break
            print(data)
            connection.sendall(data)