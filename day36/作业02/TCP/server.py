import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
while True:
    conn, client_addr = server.accept()
    while True:
        try:
            data = conn.recv(10)
            if len(data) == 0:
                break
            print(data.decode('utf-8'))
            conn.send("刚收到消息：".encode('utf-8'))
            conn.send(data)
        except Exception as e:
            print(e)
            break
server.close()