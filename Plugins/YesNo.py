from Plugins.Base import BasePlugin as base
import random


class YesNoPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'ДаНет'
        self.description = 'Выбирает либо да, либо нет'
        self.words = ["данет", "дн", "yesno", "yd"]

    def func(self):
        try:
            m = [
                ["Да", "Конечно", "Так точно", "А ты сомневался?", "Обязательно"],
                ["Нет", "Ты что, совсем?", "Сомневаюсь", "Никогда", "Не знаю.."]
            ]
            self.result['message'] = random.choice(random.choice(m))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
