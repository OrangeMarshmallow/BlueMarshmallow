from Plugins.Base import BasePlugin as base
from googletrans import Translator
from weather import Weather, Unit
from Utils import Engine as UEngine
from VK import VK


class WeatherPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Погода'
        self.description = 'Показывает погоду в городе'
        self.words = ["погода", "weather"]

    def func(self):
        if self.text == '':
            try:
                self.text = VK().Users().get(user_ids=self.user, fields='city')[0]['city']['title']
            except Exception as e:
                self.result['message'] = 'Некорректный город или ваш город скрыт.\n' + str(e)
                return True
        try:
            _weather = Weather(unit=Unit.CELSIUS)
            time = 1
            loc = ''
            if ' ' in self.text:
                res = self.text.split()
                ok = False
                for i in res:
                    if UEngine.is_int(i):
                        ok = True
                if ok:
                    if UEngine.is_int(res[0]):
                        loc += res[1]
                        time += int(res[0])
                    else:
                        loc += res[0]
                        time += int(res[1])
                else:
                    self.result['message'] = 'Введите город и количество дней.'
                    return True
            else:
                if UEngine.is_int(self.text):
                    time += int(self.text)
                    try:
                        loc += VK().Users().get(user_ids=self.user, fields='city')[0]['city']['title']
                    except Exception as e:
                        self.result['message'] = 'Некорректный город или ваш город скрыт.\n' + str(e)
                        return True
                else:
                    loc += self.text
            location = _weather.lookup_by_location(loc)
            forecasts = location.forecast
            index = 0
            _str = loc + ':\n'
            for forecast in forecasts:
                if index < time:
                    if not index:
                        _str += '(Today) '
                    _str += f'{forecast.date}: {forecast.text} ({forecast.low}-{forecast.high})\n'
                index += 1
            translator = Translator()
            self.result['message'] = translator.translate(_str, src='en', dest='ru').text
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
