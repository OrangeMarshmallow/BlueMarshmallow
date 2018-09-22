from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine


class PrisonPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Тюрьма'
        self.description = 'Отправляет случайную пикчу, может ебнутую, может и нет'
        self.words = ["тюрьма", "prison"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            self.result['attachment'] = UEngine.get_random_wall_picture(-73692762, int(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
