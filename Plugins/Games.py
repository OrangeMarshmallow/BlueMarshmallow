from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from bs4 import BeautifulSoup
import requests
import random


class GamesPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Игры'
        self.description = 'Отправляет случайную игру'
        self.words = ["игры", "games"]

    def func(self):
        try:
            r = requests.get(f'https://kanobu.ru/games/popular/?page={random.randint(1,2684)}')
            soup = BeautifulSoup(r.text, 'html5lib')
            mas = [i.find('div', {'class': 'h2'}).text for i in soup.find_all('div', {'class': 'c-game__option'})]
            if len(str(self.text)) > 0:
                if UEngine.is_int(self.text):
                    if int(self.text) < 0:
                        self.text = 1
                    if int(self.text) > 18:
                        self.text = 18
                    _str = ''
                    for i in range(int(self.text)):
                        game = random.choice(mas)
                        _str += str(i+1) + '. ' + game[1:len(game)-1] + '\n'
                        mas.remove(game)
                    self.result['message'] = _str
            else:
                self.result['message'] = random.choice(mas)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
