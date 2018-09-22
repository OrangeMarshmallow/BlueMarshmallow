from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine


class AdminList(base):
    def __init__(self):
        super().__init__()
        self.name = 'Админы'
        self.description = 'Выводит администраторов беседы'
        self.words = ["админы", "admins"]

    def func(self):
        try:
            _str = 'Администраторы:\n'
            for user in db.admins:
                _str += f'~ {UEngine.get_link_by_id(user)}'
                if UEngine.get_user_online(user):
                    _str += ' [online]'
                _str += '\n'
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
