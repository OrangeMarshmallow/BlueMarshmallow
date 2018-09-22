from Plugins.Base import BasePlugin as base
from bs4 import BeautifulSoup
import requests
import random


class BiblePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Библия'
        self.description = 'Отправляет случайную строку из Библии'
        self.words = ["библия", "bible"]

    def func(self):
        try:
            while True:
                a = random.randint(1, 65)
                b = random.randint(1, 50)
                c = random.randint(1, 50)
                try:
                    r = requests.get('https://www.bibleonline.ru/bible/rus/' + str(a) + '/' + str(b))
                    soup = BeautifulSoup(r.text, 'html5lib')
                    name = soup.find("h1", {"class": "sprite"}).text
                    line = soup.find_all("li", {"class": 'v'})[c].text
                    self.result['message'] = name[:len(name)] + '\n' + str(c) + '. ' + line
                    return True
                except Exception as e:
                    print('Error: ' + str(e))
        except Exception as e:
            self.result['message'] = str(e)
            return False
