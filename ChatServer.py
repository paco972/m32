import socket
import threading

# Connection Data
HOST = ''
PORT = 55555

# Starting listeningSocket
listeningSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listeningSocket.bind((HOST, PORT))
listeningSocket.listen()

# Lists For Clients and Their noms
clients = []
noms = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nom = noms[index]
            broadcast('{} a quitté le chat!'.format(nom).encode('utf-8'))
            noms.remove(nom)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = listeningSocket.accept()
        print("Nouvelle connexion avec {}".format(str(address)))

        # Request And Store nom
        client.send('NOM'.encode('utf-8'))
        nom = client.recv(1024).decode('utf-8')
        noms.append(nom)
        clients.append(client)

        # Print And Broadcast nom
        print("Nom: {}".format(nom))
        broadcast("{} a rejoint le chat!".format(nom).encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()