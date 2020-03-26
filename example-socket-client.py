import socket

HOST = socket.gethostname()   # The remote host
PORT = 50001             # The same port as used by the server
with socket.socket() as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))