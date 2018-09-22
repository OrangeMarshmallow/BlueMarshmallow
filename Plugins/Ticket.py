from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class TicketPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Билет'
        self.description = 'Генерирует билет, который может оказаться счастливым'
        self.words = ["билет", "ticket"]

    def func(self):
        try:
            mode = '-'
            _code = self.text
            _id = self.user
            if not _code is None:
                if len(str(_code)) > 0:
                    if _code.isdigit():
                        if UEngine.is_int(int(_code) / int(_id)):
                            mode = '+'
            if mode == '+':
                p = 0
                while True:
                    p += 1
                    num = ''
                    one = 0
                    two = 0
                    for i in range(6):
                        n = random.randint(0, 9)
                        num += str(n)
                        if i < 3:
                            one += n
                        else:
                            two += n
                    if one == two:
                        self.result['message'] = f'[{p}] Lucky: {str(num)}'
                        return True
            else:
                num = ''
                one = 0
                two = 0
                for i in range(6):
                    n = random.randint(0, 9)
                    num += str(n)
                    if i < 3:
                        one += n
                    else:
                        two += n
                if one == two:
                    self.result['message'] = f'Lucky: {str(num)}'
                else:
                    self.result['message'] = f'Unlucky: {str(num)}'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
