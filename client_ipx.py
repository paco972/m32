from ast import While
import socket
from urllib import response

# Connecting To Server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('192.168.1.15', 9870))

# Listening to Server and Sending name
def receive():
    try:
        # Receive Message From Server
        response = clientSocket.recv(1024).decode('utf-8')
    except:
        # Close Connection When Error
        response = "Erreur!"
        clientSocket.close()
    finally:
        return response

# Send Messages To Server
def write(commande):
    clientSocket.send(commande.encode('utf-8'))

while True:
    commande = format(input('Commande : '))
    if 'stop' in commande:
        break
    write(commande)
    print(receive())
