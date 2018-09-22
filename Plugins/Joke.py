from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from bs4 import BeautifulSoup
import requests


class JokePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Анекдот'
        self.description = 'Пытается пошутить'
        self.words = ["шутка", "анекдот", "joke"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            result = ''
            for i in range(int(self.text)):
                r = requests.get('https://randstuff.ru/joke/')
                soup = BeautifulSoup(r.text, 'html5lib')
                _str = soup.find("table", {"class": "text"}).text
                result += str(i+1) + '. ' + _str + '\n\n'
            self.result['message'] = result
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
