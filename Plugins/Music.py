from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class MusicPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Музыка'
        self.description = 'Отправляет случайную музыку'
        self.words = ["музыка", "music"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            groups = [
                -27895931,
                -22866546,
                -35983383,
                -42440233,
                -48713061,
                -26515827,
                -78354614,
                -78849814,
                -116805844,
                -96801065,
                -95941375,
                -20060920,
                -25008403,
                -31257157,
                -10830340,
                -22952938
            ]
            self.result['attachment'] = UEngine.get_random_wall_music(random.choice(groups), int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
