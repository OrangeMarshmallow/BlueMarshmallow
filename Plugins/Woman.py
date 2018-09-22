from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class WomanPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Девушка'
        self.description = 'Отправляет рандомную девушку'
        self.words = ["девушка", "сиськи", "попа", "жопа", "секс", "woman", "female", "boobs", "ass", "sex"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            groups = [
                -46764887,
                -80461135,
                -62846302,
                -56861816
            ]
            self.result['attachment'] = UEngine.get_random_wall_picture(random.choice(groups), int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
