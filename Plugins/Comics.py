from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine


class ComicsPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Комиксы'
        self.description = 'Присылает случайный комикс'
        self.words = ["комикс", "comics"]

    def func(self):
        try:
            if not UEngine.is_int(self.text):
                self.text = 1
            if int(self.text) > 10:
                self.text = 10
            while True:
                a = UEngine.get_random_wall_picture(-74382159, int(self.text))
                if len(a) > 1:
                    self.result['attachment'] = a
                    return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
