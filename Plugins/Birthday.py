from Plugins.Base import BasePlugin as base
from VK import VK


class BirthdayPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Дни рождения'
        self.description = 'Выводит дни рождения'
        self.words = ["деньрождения", "др", "birthday"]

    def func(self):
        try:
            if str(self.text) == '':
                users = VK().Messages().get_chat(fields='bdate')['users']
                _str = 'Дни рождения:\n'
                for user in users:
                    _str += user['first_name'] + ' ' + user['last_name'] + ': '
                    if 'bdate' in user:
                        _str += user['bdate']
                    else:
                        _str += 'скрыто'
                    _str += '\n'
                    self.result['message'] = _str
            else:
                try:
                    u = VK().Users().get(user_ids=self.text, name_case='gen', fields='bdate')[0]
                    _str = 'День рождения ' + u['first_name'] + ' ' + u['last_name'] + ': '
                    if 'bdate' in u:
                        _str += u['bdate']
                    else:
                        _str += 'скрыт'
                    self.result['message'] = _str
                except Exception as e:
                    self.result['message'] = 'Введите корректный id: ' + str(e)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
