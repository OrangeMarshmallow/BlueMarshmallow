from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class SpidersPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Пауки'
        self.description = 'Присылает случайную пикчу с пауком'
        self.words = ["паук", "spider"]

    def func(self):
        try:
            if not UEngine.is_int(self.text):
                self.text = 1
            if int(self.text) > 10:
                self.text = 10
            while True:
                groups = [
                    -36292619,
                    -4186257
                ]
                a = UEngine.get_random_wall_picture(random.choice(groups), int(self.text))
                if len(a) > 1:
                    self.result['attachment'] = a
                    return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
