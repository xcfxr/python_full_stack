import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
while True:
    try:
        text = input("请输入需要发送的内容：")
        # if len(text) == 0:
        #     continue
        client.send('hello'.encode('utf-8'))
        client.send('world'.encode('utf-8'))  ## 发生粘包问题
        print(client.recv(1024).decode('utf-8'))
    except Exception as e:
        break
client.close()