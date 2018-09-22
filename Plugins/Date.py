from Plugins.Base import BasePlugin as base
import datetime
import random
import time


class DatePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Дата'
        self.description = 'Выбирает случайную дату'
        self.words = ["дата", "когда", "date"]

    def func(self):
        try:
            self.result['message'] = datetime.datetime.fromtimestamp(time.mktime(datetime.datetime.now().timetuple()) +
                                                                     random.randint(0, 2412016382))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            self.result['message'] = e
            return False
