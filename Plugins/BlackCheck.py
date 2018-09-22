from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine
from VK import VK


class BlackCheckPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Проверка на ЧС'
        self.description = 'Проверяет пользователей на нахождение в черном списке'
        self.words = ["чспроверка", "blackcheck"]
        self.level = 'am'

    def func(self):
        try:
            users = VK().Messages().get_chat()['users']
            _str = 'Пользователи, найденые в чс:\n'
            index = 0
            for _user in users:
                if int(_user) in db.black:
                    index += 1
                    _str += str(index) + '. ' + UEngine.get_username_by_id(_user) + '\n'
                    VK().Messages().remove_chat_user(user_id=_user)
            if index > 0:
                self.result['message'] = _str
            else:
                self.result['message'] = 'Пользователей из черного списка не найдено.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
