from Plugins.Base import BasePlugin as base
from bs4 import BeautifulSoup
import requests
import random


class HabrPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Хабр'
        self.description = 'Отправляет случайную статью из хабра'
        self.words = ["хабр", "habr"]

    def func(self):
        try:
            soup = ''
            temp_len = 5000
            _str = ''
            pid = 0
            while temp_len > 4096:
                _str = ''
                status = False
                while not status:
                    pid = random.randint(350000, 413003)
                    r = requests.get('https://habr.com/post/' + str(pid) + '/')
                    soup = BeautifulSoup(r.text, 'html5lib')
                    if not soup.find("span", {"class": "post__title-text"}):
                        status = False
                    else:
                        status = True
                _str += 'Источник: ' + 'https://habr.com/post/' + str(pid) + '/\n\n'
                _str += soup.find("span", {"class": "post__title-text"}).text + ':\n'
                _str += soup.find("div", {"class": "post__text"}).text + '\n\nДата поста: '
                _str += soup.find("span", {"class": "post__time"}).text
                temp_len = len(_str)
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
