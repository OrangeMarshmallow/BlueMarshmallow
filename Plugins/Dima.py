from Plugins.Base import BasePlugin as base
import datetime
import time


class DimaPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Димооооон'
        self.description = 'Показывает всю информацию об армии'
        self.words = ["дима", "димон", "димооон", "dima"]

    def func(self):
        try:
            start_timestamp = 1530780785
            end_timestamp = start_timestamp + 31536000
            now_timestamp = time.mktime(datetime.datetime.now().timetuple())

            t1 = datetime.datetime.fromtimestamp(start_timestamp)
            t2 = datetime.datetime.fromtimestamp(now_timestamp)
            t3 = datetime.datetime.fromtimestamp(end_timestamp)

            t33 = datetime.date(int(t3.year), int(t3.month), int(t3.day))
            t22 = datetime.date(int(t2.year), int(t2.month), int(t2.day))
            t11 = datetime.date(int(t1.year), int(t1.month), int(t1.day))

            t31 = str(t33 - t11).split()[0]
            t21 = str(t22 - t11).split()[0]
            t32 = int(t31) - int(t21)

            res = ''
            res += f'Начал службу: {t1.day}-{t1.month}-{t1.year}\n'
            res += f'Сейчас: {t2.day}-{t2.month}-{t2.year}\n'
            res += f'Конец службы: {t3.day}-{t3.month}-{t3.year}\n'
            res += f'Всего дней: {t31}\n'
            res += f'Осталось дней: {t32}\n'
            res += f'Прошло дней: {t21}\n'
            self.result['message'] = res
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
