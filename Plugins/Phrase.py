from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from bs4 import BeautifulSoup
import requests


class PhrasePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Фраза'
        self.description = 'Отправляет случайную фразу'
        self.words = ["фраза", "phrase"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            result_mes = ''
            for i in range(int(self.text)):
                r = requests.get('https://genword.ru/generators/winged/')
                soup = BeautifulSoup(r.text, 'html5lib')
                result = str(soup.find("span", {"class": "result"}))
                source = str(soup.find("div", {"class": "source"}))
                result = result[result.find('>') + 1:result.find('/') - 1]
                source = source[source.find('>') + 1:source.find('/') - 1]
                result_mes += str(i+1) + '. ' + source + ': ' + result + '\n\n'
            self.result['message'] = result_mes
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
