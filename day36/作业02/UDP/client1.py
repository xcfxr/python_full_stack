import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 8080)
while True:
    text = input("请输入发送的内容：")
    client.sendto(text.encode('utf-8'), server_addr)
    text, _ = client.recvfrom(1024)