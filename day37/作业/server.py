import json
import os.path
import socketserver
import struct


class MyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        header_size = struct.unpack('i', self.request.recv(4))[0]
        header = self.request.recv(header_size)
        header = json.loads(header)
        if header['task'] == '1':
            target_path = os.path.join('server_upload', header['name'])
            total_size = os.path.getsize(target_path)
            print('所传输文件大小为%dBytes' % total_size)
            total_size = struct.pack('i', total_size)
            self.request.send(total_size)
            with open(target_path, 'rb') as f:
                for line in f:
                    self.request.send(line)
        else:
            target_path = os.path.join('server_download', header['name'])
            total_size = header['size']
            print('所接受文件大小为%dBytes' % total_size)
            recv_size = 0
            with open(target_path, 'wb') as f:
                while recv_size < total_size:
                    line = self.request.recv(1024)
                    recv_size += len(line)
                    f.write(line)


server = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), MyRequestHandler)
server.serve_forever()