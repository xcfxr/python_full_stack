import subprocess
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
while True:
    conn, client_addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024)
            print(cmd.decode('utf-8'))
            obj = subprocess.Popen(cmd.decode('utf-8'),shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            right_res = obj.stdout.read()
            wrong_res = obj.stderr.read()
            conn.send(right_res + wrong_res)
        except Exception as e:
            print(e)
            break
