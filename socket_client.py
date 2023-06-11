import asyncio
import socket
import sys


class Signaler:
    """
    遥控器
    发送 socket、接收 socket
    前进、后退、左转、右转
    """

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.socket_client = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
        self.socket_client.connect(
                (self.HOST, self.PORT)
            )
        print(self.socket_client)

    # def connect(self) -> object:
    #     try:
    #         socket_client = socket.socket(
    #             socket.AF_INET,
    #             socket.SOCK_STREAM
    #         ).connect(
    #             (self.HOST, self.PORT)
    #         )
    #         print('Socket Client 连接成功')
    #         return socket_client
    #     except socket.error as msg:
    #         print(
    #             'Socket 连接失败，错误代码：' + str(msg[0]) + '，错误信息：' + msg[
    #                 1])
    #         sys.exit()

    async def send(self, cmd: str):
        self.socket_client.send(cmd.encode('utf-8'))
        print('Socket Client 发出消息')
        data_reply = self.socket_client.recv(1024).decode('utf-8')
        print('Socket Client 收到消息：' + data_reply)
        return data_reply

    async def receive(self):
        """
        开一个线程，持续接收 服务端消息
        :return:
        """
        pass

    async def forward(self):
        """
        前进
        :return:
        """
        result = await self.send('forward')
        return result

    async def backward(self):
        """
        后退
        :return:
        """
        result = await self.send('backward')
        return result

    async def turn_left(self):
        """
        左转
        :return:
        """
        result = await self.send('turn_left')
        return result

    async def turn_right(self):
        """
        右转
        :return:
        """
        result = await self.send('turn_right')
        return result

    async def close(self):
        """
        关闭连接
        :return: bool
        """
        result = await self.send('888close')
        if result == 'ok_close':
            print('Socket Client 关闭连接')
            self.socket_client.close()
            return True
        else:
            print('Socket Client 关闭连接失败')
            return False


# if __name__ == '__main__':
#     my_control = Signaler(host='119.29.143.178', port=9592)
#
#     for i in range(200):
#         print(i)
#         asyncio.run(my_control.forward(i))
#         asyncio.run(my_control.backward(i))
#         asyncio.run(my_control.turn_left(i))
#         asyncio.run(my_control.turn_right(i))

