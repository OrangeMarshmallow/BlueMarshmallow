from Plugins.Base import BasePlugin as base
from pycbrf.toolbox import ExchangeRates
from Utils import Engine as UEngine
import datetime


class CurrencyPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Валюта'
        self.description = 'Говорит курс валют на сегодняшний день'
        self.words = ["курс", "валюта", "currency"]

    def func(self):
        try:
            a = 1
            if UEngine.is_int(self.text):
                a *= int(self.text)
            today = str(datetime.date.today())
            rates = ExchangeRates(today)
            val = ['USD', 'EUR']
            _str = f'[{str(today)}] Курс валют:\n'
            for v in val:
                data = rates[v]
                _str += f'{data.name}: {data.value * a}\n'
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
