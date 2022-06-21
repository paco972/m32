#!/usr/bin/python3
import socket
from datetime import datetime

HOST = b'time-c.nist.gov'
PORT = 13

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
#print(data.decode("utf-8"))

espace1 = data.find(b' ')

date = data[espace1+1:espace1+9]
date_formatee = datetime.strptime(date.decode("utf-8"), '%y-%m-%d').strftime('%d/%b/%Y')
print('Date: ' + date_formatee)

heure = data[espace1+10:espace1+18]
print('Heure: ' + heure.decode("utf-8"))

s.close()
