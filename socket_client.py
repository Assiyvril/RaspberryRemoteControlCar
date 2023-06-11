import socket
import sys
import time

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Client 创建成功')

HOST = '192.168.31.177'
PORT = 9592

try:
    socket_client.connect((HOST, PORT))
except socket.error as msg:
    print('Socket Client 连接失败，错误代码：' + str(msg[0]) + '，错误信息：' + msg[1])
    sys.exit()

print('Socket Client 连接成功')

for i in range(5):
    msg = f'客户端请求连接 {i}'.encode('utf-8')
    socket_client.send(msg)
    print('Socket Client 发出消息')
    data = socket_client.recv(1024).decode('utf-8')
    print('Socket Client 收到消息：' + data)
    time.sleep(1)

# 发出关闭连接请求
socket_client.send('888close'.encode('utf-8'))
print('Socket Client 发出关闭连接请求')
close_data = socket_client.recv(1024).decode('utf-8')
print('Socket Client 收到关闭连接请求：' + close_data)

if close_data == 'ok_close':
    print('Socket Client 关闭连接')
    socket_client.close()
