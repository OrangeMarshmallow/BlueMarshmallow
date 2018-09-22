from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import random


class SatanBiblePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Библия Сатаны'
        self.description = 'Отправляет случайную строку из Библии Сатаны'
        self.words = ["сатана", "satan"]

    def func(self):
        try:
            f = open('DB\\satan.txt')
            text = f.read()
            dots = [i for i in range(len(text)) if text[i] in '.']
            res = ''
            if len(str(self.text)) > 0:
                if UEngine.is_int(self.text):
                    if int(self.text) < 0:
                        self.text = 1
                    if int(self.text) > 10:
                        self.text = 10
            else:
                self.text = 1
            for i in range(int(self.text)):
                tmp_len = 0
                while tmp_len < 3:
                    d = random.randint(0, len(dots))
                    res += str(i+1) + '. ' + text[dots[d]+2:dots[d+1]+1] + '\n'
                    tmp_len = len(text[dots[d]+2:dots[d+1]+1])
            self.result['message'] = res
            f.close()
        except Exception as e:
            self.result['message'] = str(e)
            return False
