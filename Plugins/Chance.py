from Plugins.Base import BasePlugin as base
import random


class ChancePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Шанс'
        self.description = 'Говорит шанс чего-либо'
        self.words = ["шанс", "chance"]

    def func(self):
        try:
            self.result['message'] = str(random.randint(0, 10000) / 100) + '%'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
