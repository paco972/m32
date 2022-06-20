import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 63000  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((HOST, PORT))
    message = bytes('Serveur es-tu là ?','utf-8')
    server.sendall(message)
    data = server.recv(1024)
    print(data.decode('utf-8'))
