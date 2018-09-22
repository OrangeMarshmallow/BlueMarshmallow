from Plugins.Base import BasePlugin as base
from Settings import DataBase as db


class QuestionPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Обращение к админу'
        self.description = 'Позволяет напрямую написать админам.'
        self.words = ["обращение", "вопрос", "question"]

    def func(self):
        try:
            users = db.admins
            _str = 'Админы, ' + self.text + '\n'
            for user in users:
                _str += f"@id{user} (឵.)"
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
