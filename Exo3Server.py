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
            message = clientSocket.recv(1024).decode('utf-8')
            if 'fini' in message:
                break
            print(message)
            response = bytes(input('Réponse : '), 'utf-8')
            clientSocket.sendall(response)
