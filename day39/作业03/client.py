import socket
client = socket.socket()
client.connect(('127.0.0.1', 8080))
while True:
    client.send(b'hello world')
    print(client.recv(1024))