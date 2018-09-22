from Plugins.Base import BasePlugin as base
import random


class WherePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Место'
        self.description = 'Выбирает случайное место'
        self.words = ["где", "куда", "откуда", "место", "where"]

    def func(self):
        try:
            self.result['lat'] = random.randint(-90000000, 90000000) / 1000000
            self.result['long'] = random.randint(-180000000, 180000000) / 1000000
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
