from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from bs4 import BeautifulSoup
import requests


class TaglinePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Слоган'
        self.description = 'Отправляет случайный слоган'
        self.words = ["слоган", "tagline"]

    def func(self):
        if not UEngine.is_int(self.text):
            self.text = 1
        if int(self.text) > 10:
            self.text = 10
        try:
            result_mes = ''
            for i in range(int(self.text)):
                r = requests.get('https://genword.ru/generators/slogan/')
                soup = BeautifulSoup(r.text, 'html5lib')
                result = str(soup.find("span", {"class": "result"}))
                result = result[result.find('>') + 1:result.find('/') - 1]
                result_mes += str(i+1) + '. ' + result + '.\n\n'
            self.result['message'] = result_mes
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
