from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine


class PasswordPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Пароль'
        self.description = 'Генерирует пароль для пользователя'
        self.words = ["пароль", "password"]
        self.level = 'a'

    def func(self):
        try:
            self.result['message'] = UEngine.get_password(UEngine.get_user_id(self.text))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
