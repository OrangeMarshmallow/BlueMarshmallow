from Plugins.Base import BasePlugin as base
from bs4 import BeautifulSoup
import requests
import re


class FootballPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Футбол'
        self.description = 'Выводит информацию о турнирной таблице ЧМ 2018 по футболу'
        self.words = ["футбол", "football"]

    def func(self):
        try:
            r = requests.get('https://www.championat.com/football/_worldcup/1589/table/all/playoff.html')
            soup = BeautifulSoup(r.text, 'html5lib')
            _str = soup.find("div", {"class": "sport__table"}).text
            _str = _str.replace('  ', '')
            _str = _str.replace('\n\n', '')
            _str = _str.replace('\n—', ' — ')
            _str = _str.replace('—\n', ' — ')

            res1 = re.compile('A0\d').findall(_str)
            res2 = re.compile('QF\d').findall(_str)
            res3 = re.compile('SF\d').findall(_str)
            res4 = re.compile('F\d').findall(_str)
            res = res1 + res2 + res3 + res4

            for s in res:
                _str = _str.replace(s, '')

            result = re.compile('\w\d:\d\n').findall(_str)
            for s in result:
                s = s[1:len(s) - 1]
                _str = _str.replace(s, f' ({s})')

            dt = re.compile('\d{2}.\d{2}.\d{4}\n').findall(_str)
            for s in dt:
                _str = _str.replace(s, f'[{s[:len(s)-1]} , ')
            tm = re.compile('\d{2}:\d{2}\n|\d{2}:\d{2}\w').findall(_str)
            for s in tm:
                _str = _str.replace(s, f'{s[:len(s)-1]}] {s[len(s)-1:]}')
            _str = _str.replace('–:–', ' (None)')

            winner = re.compile('\n\w+\n\[').findall(_str)
            for s in winner:
                _str = _str.replace(s, '\n[')

            sch = re.compile('\n\d:\d').findall(_str)
            for s in sch:
                _str = _str.replace(s, f' ({s[1:]})\n')

            dop1 = re.compile('\n \(None\)').findall(_str)
            for s in dop1:
                _str = _str.replace(s, ' ' + s[2:])

            dop2 = re.compile(' — \n').findall(_str)
            for s in dop2:
                _str = _str.replace(s, ' — ')

            dop3 = re.compile('\] \w+').findall(_str)
            for s in dop3:
                _str = _str.replace(s, ']\n')

            dop4 = re.compile('/\D+').findall(_str)
            for s in dop4:
                _str = _str.replace(s, s[1:])

            dop5 = re.compile(']\n ').findall(_str)
            for s in dop5:
                _str = _str.replace(s, ']\n')

            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
