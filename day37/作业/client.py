import json
import os
import socket
import struct
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))
while True:
    print('''
    请选择任务类型：
    0：上传
    1：下载
    ''')
    header = {'task': input(), 'size': None, 'name': None}
    if header['task'] == '0':
        file_name = input('请输入上传文件名：')
        target_path = os.path.join('client_upload', file_name)
        header['size'] = os.path.getsize(target_path)
        header['name'] = file_name
    elif header['task'] == '1':
        file_name = input('请输入下载文件名：')
        target_path = os.path.join('client_download', file_name)
        header['name'] = file_name

    json_obj = json.dumps(header)
    bytes_of_json = struct.pack('i', len(json_obj.encode('utf-8')))
    client.send(bytes_of_json)
    client.send(json_obj.encode('utf-8'))
    if header['task'] == '1':
        target_path = os.path.join('client_download', file_name)
        file_size = client.recv(4)
        file_size = struct.unpack('i', file_size)[0]
        receive_size = 0
        with open(target_path, 'wb') as f:
            while receive_size < file_size:
                line = client.recv(1024)
                f.write(line)
                receive_size += len(line)

    else:
        with open(target_path, 'rb') as f:
            for line in f:
                client.send(line)