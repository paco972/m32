import socket

HOST = ""  # Standard loopback interface address (localhost)
PORT = 63000  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024) 
        conn.sendall(data + (bytes('\nPrésent', 'utf-8')))
        print(data)