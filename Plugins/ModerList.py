from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine


class ModerList(base):
    def __init__(self):
        super().__init__()
        self.name = 'Модеры'
        self.description = 'Выводит модераторров беседы'
        self.words = ["модеры", "moders"]

    def func(self):
        try:
            _str = 'Модераторы:\n'
            for user in db.moders:
                _str += f'~ {UEngine.get_link_by_id(user)}'
                if UEngine.get_user_online(user):
                    _str += ' [online]'
                _str += '\n'
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
