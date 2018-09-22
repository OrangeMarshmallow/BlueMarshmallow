from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class ITPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'IT'
        self.description = 'Отправляет рандомный мем про ИТ'
        self.words = ["ит", "it"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            groups = [
                -80799846,
                -146203367,
                -72495085
            ]
            self.result['attachment'] = UEngine.get_random_wall_picture(random.choice(groups), int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
