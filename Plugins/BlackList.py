from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine


class BlackList(base):
    def __init__(self):
        super().__init__()
        self.name = 'Черный список'
        self.description = 'Выводит людей из черного списка'
        self.words = ["черныйсписок", "blacklist"]
        self.level = 'am'

    def func(self):
        try:
            _str = 'Черный список:\n'
            for user in db.black:
                _str += f'{UEngine.get_username_by_id(user)}\n'
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
