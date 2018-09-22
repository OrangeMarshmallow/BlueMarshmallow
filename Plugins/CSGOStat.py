from Plugins.Base import BasePlugin as base
import requests
from bs4 import BeautifulSoup


class CSGOStatPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'CSGO stat'
        self.description = 'Отправляет общую статистику по CSGO'
        self.words = ["csgostat"]

    def func(self):
        try:
            r = requests.get('https://csgo-stats.com/')
            soup = BeautifulSoup(r.text, 'html5lib')
            _str = soup.find("div", {"class": "matchmaking-status online"}).text
            _str = _str.replace('   ', '\n')
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
