from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from VK import VK


class OnlinePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Онлайн'
        self.description = 'Показывает пользователей в сети'
        self.words = ["онлайн", "online"]

    def func(self):
        try:
            response = VK().Messages().get_chat(fields='online')['users']
            _str = ''
            for user in response:
                if int(user['online']):
                    _str += f'{user["first_name"]} {user["last_name"]}'
                    if int(user['id']) in db.admins:
                        _str += ' [Admin]'
                    elif int(user['id']) in db.moders:
                        _str += ' [Moder]'
                    _str += '\n'
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
