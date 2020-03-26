import socket

HOST = socket.gethostname()
PORT = 50001
s = socket.socket()

s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
with conn:
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)