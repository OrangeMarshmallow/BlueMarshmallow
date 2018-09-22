from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class QuotePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Цитата'
        self.description = 'Отправляет случайную пацанскую цитатку'
        self.words = ["пацан", "цитата", "цитатка", "quote"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            groups = [
                -27456813,
                -157341954,
                -35927256,
                -156666557
            ]
            while True:
                a = UEngine.get_random_wall_post(random.choice(groups), int(self.text))
                if len(a) > 1:
                    self.result['message'] = a
                    return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
