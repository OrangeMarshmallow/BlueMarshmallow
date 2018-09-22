from Plugins.Base import BasePlugin as base
import random


class CoinPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Монетка'
        self.description = 'Говорит на какую сторону упадет монетка'
        self.words = ["монетка", "coin"]

    def func(self):
        try:
            m = [
                'Орел',
                'Решка',
                'Ребро))0)'
            ]
            r = random.randint(0, 100)
            s = ''
            if r < 11:
                s += m[2]
            elif (r > 10) and (r < 56):
                s += m[1]
            else:
                s += m[0]
            self.result['message'] = s
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
