import socket
from multiprocessing import Process


def conn_process(server):
    while True:
        conn, addr = server.accept()
        while True:
            try:
                data = conn.recv(1024)
                conn.send(data.upper())
            except ConnectionResetError as e:
                print('远程连接断开')
                break
        conn.close()


if __name__ == '__main__':
    server = socket.socket()
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    for i in range(5):
        Process(target=conn_process, args=(server, )).start()