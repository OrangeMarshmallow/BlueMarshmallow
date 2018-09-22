from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from VK import VK
import random


class WhoPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Кто'
        self.description = 'Выбирает случайного человека из беседы'
        self.words = ["кто", "who"]

    def func(self):
        try:
            if random.randint(0, 100) <= 10:
                self.result['message'] = 'Никто'
            else:
                self.result['message'] = UEngine.get_link_by_id(random.choice(VK().Messages().get_chat()['users']))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
