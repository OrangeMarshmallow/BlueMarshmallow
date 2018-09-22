from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from bs4 import BeautifulSoup
import requests


class WisdomPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Мудрость'
        self.description = 'Говорит случайную мудрость'
        self.words = ["мудрость", "wisdom"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            result = ''
            for i in range(int(self.text)):
                r = requests.get('https://randstuff.ru/saying/')
                soup = BeautifulSoup(r.text, 'html5lib')
                _str = soup.find("table", {"class": "text"}).text
                t = _str[0:_str.find('—')]
                a = _str[_str.find('—') + 1:len(_str) + 1]
                a = a + ': ' + t
                result += str(i+1) + '. ' + a + '\n\n'
            self.result['message'] = result
        except Exception as e:
            self.result['message'] = str(e)
            return False
