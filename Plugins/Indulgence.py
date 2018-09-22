from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine


class IndulgencePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Индульгенция'
        self.description = 'Отправляет случайный пост из Индульгенции'
        self.words = ["индульгенция", "indulgence", "indulgencia"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            self.result['message'] = UEngine.get_random_wall_post(-44554509, int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
