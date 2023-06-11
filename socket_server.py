"""
启动一个socket服务端
"""
import socket
import sys

HOST = ''
PORT = 9592

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Server 创建成功')

try:
    socket_server.bind((HOST, PORT))
except socket.error as msg:
    print('绑定失败，错误代码：' + str(msg[0]) + '，错误信息：' + msg[1])
    sys.exit()

print('Socket Server 绑定成功')

socket_server.listen(10)
print('Socket Server 正在监听')
conn, addr = socket_server.accept()

while True:

    print('Socket Server 检测到客户端链接 连接地址：' + addr[0] + '：' + str(addr[1]))
    data = conn.recv(1024).decode('utf-8')
    print('Socket Server 收到客户端消息：' + data)
    if data == '888close':
        print('Socket Server 收到关闭连接请求')
        conn.send('ok_close'.encode('utf-8'))
        print('Socket Server 发出关闭连接请求')
        conn.close()
        print('Socket Server 关闭连接')
        break
    conn.send(f'欢迎访问Socket Server, 已收到你发来的 {data}'.encode('utf-8'))

