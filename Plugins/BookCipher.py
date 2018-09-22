from Plugins.Base import BasePlugin as base
import random


class BookCipherPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Книжный шифр'
        self.description = 'Отправляет строку, зашифрованную книжный шифром'
        self.words = ["книга", "book"]

    def func(self):
        try:
            if self.mode == '+':
                f = open('DB\\text.txt')
                text = f.read()
                fin = ''
                for j in self.text:
                    fin += str(int(random.choice([i for i in range(len(text)) if text[i] == j])) ^ 133777) + ':'
                self.result['message'] = fin[:len(fin)-1]
            elif self.mode == '-':
                f = open('DB\\text.txt')
                text = f.read()
                fin = self.text.split(':')
                for i in range(len(fin)):
                    fin[i] = text[int(fin[i]) ^ 133777]
                self.result['message'] = ''.join(fin)
            else:
                self.result['message'] = 'Используйте + чтобы зашифровать, - чтобы расшифровать'
        except Exception as e:
            self.result['message'] = str(e)
            return False
