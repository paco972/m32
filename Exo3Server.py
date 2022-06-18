from http import client
import socket

HOST = ""  # Any interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listeningSocket:
    listeningSocket.bind((HOST, PORT))
    listeningSocket.listen()
    clientSocket, address = listeningSocket.accept()
    print(f"Connected by {address}")
    with clientSocket:
        while True:
            data = clientSocket.recv(1024)
            if data == (b'fini\r\n'):
                break
            print(data)
            response = bytes(input('Réponse : ') + '\r\n', 'utf-8')
            clientSocket.sendall(response)