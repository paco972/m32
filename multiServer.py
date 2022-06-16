# coding: utf-8 

import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientSocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientSocket = clientSocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
        print("Connexion de %s %s" % (self.ip, self.port, ))
        data = self.clientSocket.recv(2048)
        print(data)
        self.clientSocket.close()
        print("Client déconnecté...")

listeningSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listeningSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listeningSocket.bind(("",65432))

while True:
    listeningSocket.listen(10)
    print( "En écoute...")
    (clientSocket, (ip, port)) = listeningSocket.accept()
    newThread = ClientThread(ip, port, clientSocket)
    newThread.start()