import asyncio

from signaler import Signaler


class Control:
    """
    遥控器
    监听键盘输入，发出对应信号
    """

    def __init__(self, host, port):
        self.signaler = Signaler(
            host=host,
            port=port
        )

    def listener(self):
        """
        监听键盘输入，发出对应信号
        :return:
        """
        while True:
            cmd = input('请输入指令：')
            if cmd == 'w':
                asyncio.run(self.signaler.forward())
            elif cmd == 's':
                asyncio.run(self.signaler.backward())
            elif cmd == 'a':
                asyncio.run(self.signaler.turn_left())
            elif cmd == 'd':
                asyncio.run(self.signaler.turn_right())
            elif cmd == 'qq':
                asyncio.run(self.signaler.close())
                break

            else:
                print('指令错误')
                continue
