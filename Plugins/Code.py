from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import requests
import random


class CodePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Задача'
        self.description = 'Отправляет случайную задачу по программированию'
        self.words = ["задача", "кодинг", "код", "task", "code"]

    def func(self):
        try:
            task = str(random.randint(1, 1000))
            self.result['message'] = \
                'Задача №' + task + '\n' + \
                UEngine.get_text(requests.get('http://acmp.ru/index.asp?main=task&id_task=' + task))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
