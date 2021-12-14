import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8080))
while True:
    data, client_addr = server.recvfrom(1024)
    print('收到消息%s, %s'%client_addr)
    print(data.decode('utf-8'))
    server.sendto(data.upper(), client_addr)