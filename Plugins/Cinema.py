from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine


class CinemaPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Кино'
        self.description = 'Отправляет случайное кино'
        self.words = ["кино", "фильм", "kino", "film", "cinema"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            self.result['attachment'] = UEngine.get_random_wall_video(-22798006, int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
