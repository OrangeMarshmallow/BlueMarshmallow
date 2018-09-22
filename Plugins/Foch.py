from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine


class FochPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = '4ch'
        self.description = 'Отправляет случайное видео из 4ch'
        self.words = ["4ch", "4ч", "фоч", "foch", "fo4"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            self.result['attachment'] = UEngine.get_random_wall_video(-45745333, int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
