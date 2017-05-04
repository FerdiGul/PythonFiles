import socket

Sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
Sock.connect(('192.168.1.30', 8088))
print(Sock.recv(2048).decode())
Sock.close()
