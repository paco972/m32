import socket
import threading

# Choosing Name
nom = input("Nom: ")

# Connecting To Server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 55555))

# Listening to Server and Sending name
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NOM' Send name
            message = clientSocket.recv(1024).decode('utf-8')
            if message == 'NOM':
                clientSocket.send(nom.encode('utf-8'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("Erreur!")
            clientSocket.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nom, input(''))
        clientSocket.send(message.encode('utf-8'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
