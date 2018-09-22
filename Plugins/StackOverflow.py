from Plugins.Base import BasePlugin as base
import urllib.parse


class StackOverflowPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'StackOverflow'
        self.description = 'Отправляет страницу с поиском проблема'
        self.words = ["стаковерфлоу", "стак", "оверфлоу", "со", "stackoverflow", "stack", "overflow", "so"]

    def func(self):
        try:
            self.result['message'] = 'https://stackoverflow.com/search?q=' + urllib.parse.quote(self.text)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
