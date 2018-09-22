from Plugins.Base import BasePlugin as base
import random


class BotPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Бот'
        self.description = 'Для проверки онлайна бота'
        self.words = ["бот", "bot"]

    def func(self):
        try:
            m = [
                "Привет",
                "Сап",
                "Ну что опять?",
                "Тут я",
                "Ая",
                "Что?",
                "Да здесь я",
                "Я снова пришел",
                "Я и не отходил",
                "Весь внимания",
                "Да-да, я онлайн",
                "Опять лолек надо?",
                "Лолек захотелось?))",
                "Димон, где БД"
            ]
            self.result['message'] = random.choice(m)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
