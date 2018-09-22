from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class MemePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Мем'
        self.description = 'Отправляет рандомный мем'
        self.words = ["меме", "мем", "mem", "meme"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            groups = [
                -65596623,
                -45595714,
                -75338985,
                -58158419,
                -71067613
            ]
            self.result['attachment'] = UEngine.get_random_wall_picture(random.choice(groups), int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
