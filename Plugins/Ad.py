from Plugins.Base import BasePlugin as base
from VK import VK


class AdPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Объявление'
        self.description = 'Позволяет создавать объявление для всех пользователей'
        self.words = ["объяви", "объявление", "ad"]
        self.level = 'a'

    def func(self):
        try:
            users = VK().Messages().get_chat(fields='first_name, last_name')['users']
            _str = 'Внимание, объявление: ' + self.text + '\n'
            for user in users:
                _str += f"@id{user['id']} (.)"
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
