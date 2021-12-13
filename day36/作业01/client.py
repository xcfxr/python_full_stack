import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
while True:
    cmd = input("请输入远程执行的命令：").strip()
    client.send(cmd.encode('utf-8'))
    print(client.recv(1024).decode('gbk'))