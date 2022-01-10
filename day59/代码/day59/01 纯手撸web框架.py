# 你可以将web框架理解成服务端
import socket


server = socket.socket()  # TCP  三次握手四次挥手  osi七层
server.bind(('127.0.0.1',8080))  # IP协议 以太网协议 arp协议...
server.listen(5)  # 池 ...

"""
b'GET / HTTP/1.1\r\n
Host: 127.0.0.1:8082\r\n
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n
Cookie: csrftoken=KYJnVBLPpJxwt09TOmTXzpb5qkFJwHVxVGpi0NxEGIg4z5VUuazZ1O2RMwSisu14\r\n
\r\n'


"""
while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    # print(data)  # 二进制数据
    data = data.decode('utf-8')  # 字符串
    # 获取字符串中特定的内容       正则  如果字符串有规律也可以考虑用切割
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    current_path = data.split(' ')[1]
    # print(current_path)
    if current_path == '/index':
        # conn.send(b'index heiheihei')
        with open(r'templates/01 myhtml.html', 'rb') as f:
            conn.send(f.read())
    elif current_path == '/login':
        conn.send(b'login')
    else:
        # 你直接忽略favicon.ico
        conn.send(b'hello web')
    conn.close()


