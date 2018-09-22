from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class SnakePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Змеи'
        self.description = 'Отправляет случайную змею'
        self.words = ["змея", "питон", "рептилия", "snake", "python", "reptile"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            groups = [
                -62376962,
                -113698537
            ]
            self.result['attachment'] = UEngine.get_random_wall_picture(random.choice(groups), int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
