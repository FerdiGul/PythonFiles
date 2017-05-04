
import socket

Sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
Sock.bind(('192.168.1.30', 8088))
Sock.listen(1)

while True:
    client, addr = Sock.accept()
    print(addr[0], 'is connected to the server!')
    client.send('Server loves you bro'.encode())
    client.close()
