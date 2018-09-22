from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class LoliPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Лоли'
        self.description = 'Отправляет пикчу с лолей'
        self.words = ["лоли", "лоля", "лоль", "лоликон", "loli", "lolya", "loly", "lolicon"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            groups = [
                -127518015,
                -101072212,
                -69721869,
                -111673172,
                -151443835,
                -113969740,
                -157516431
            ]
            self.result['attachment'] = UEngine.get_random_wall_picture(random.choice(groups), int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
