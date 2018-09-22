from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import requests
import codecs
import os


class HTMLPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'HTML'
        self.description = 'Отправляет код страницы'
        self.words = ["хтмл", "html"]

    def func(self):
        try:
            if len(str(self.text)):
                if not 'http' in self.text:
                    self.text = 'https://' + self.text
                f = codecs.open('DB\\Source.txt', 'wb')
                f.write(str.encode(requests.get(self.text).text))
                f.close()
                self.result['attachment'] = UEngine.doc('DB\\Source.txt')
            else:
                self.result['message'] = 'Введите сайт'
            os.remove('DB\\Source.txt')
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
