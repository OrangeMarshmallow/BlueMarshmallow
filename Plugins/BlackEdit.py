from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine


class BlackEditPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Редактирование черного списка'
        self.description = 'Позволяет редактировать черный список'
        self.words = ["черный", "black"]
        self.level = 'am'

    def func(self):
        try:
            user_id = self.text
            if len(str(user_id)) > 0:
                if not int(user_id) in db.black:
                    if self.mode == '+':
                        db.black.append(int(user_id))
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' добавлен в черный список'
                    else:
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' не состоит в черном списке'
                else:
                    if self.mode == '-':
                        db.black.remove(int(user_id))
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' удален из черного списка'
                    else:
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' уже в черном списке'
                from Plugins import BlackCheck
                BlackCheck.BlackCheckPlugin().func()
            else:
                self.result['message'] = 'Не правильная команда.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
