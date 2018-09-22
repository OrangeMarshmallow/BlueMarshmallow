from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class SchoolPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Школа'
        self.description = 'Отправляет рандомную школьницу'
        self.words = ["школа", "школьница", "school", "schoolgirl"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            groups = [
                -134982584,
                -84753006,
                -146150692,
                -126442376,
                -65144752,
                -83971955,
                -83971955
            ]
            self.result['attachment'] = UEngine.get_random_wall_picture(random.choice(groups), int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
