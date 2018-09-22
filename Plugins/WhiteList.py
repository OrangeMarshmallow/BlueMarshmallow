from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine


class WhiteList(base):
    def __init__(self):
        super().__init__()
        self.name = 'Белый список'
        self.description = 'Выводит людей из белого списка'
        self.words = ["белыйсписок", "whitelist"]
        self.level = 'am'

    def func(self):
        try:
            _str = 'Белый список:\n'
            for user in db.white:
                _str += f'{UEngine.get_link_by_id(user)}\n'
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
