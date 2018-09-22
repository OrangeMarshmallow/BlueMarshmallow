from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from Settings import DataBase as db
from Utils import Engine as UEngine


class AdminEditPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Редактирование админов'
        self.description = 'Позволяет редактировать список админов'
        self.words = ["админ", "admin"]
        self.level = 'a'

    def func(self):
        try:
            if self.user == var.czarID:
                user_id = self.text
                if len(str(user_id)) > 0 and UEngine.user_exist_in_chat(user_id):
                    if not int(user_id) in db.admins:
                        if self.mode == '+':
                            db.admins.append(int(user_id))
                            self.result['message'] = UEngine.get_link_by_id(user_id) + ' добавлен в админы'
                        else:
                            self.result['message'] = UEngine.get_link_by_id(user_id) + ' не является админом'
                    else:
                        if self.mode == '-':
                            db.admins.remove(int(user_id))
                            self.result['message'] = UEngine.get_link_by_id(user_id) + ' удален из админов'
                        else:
                            self.result['message'] = UEngine.get_link_by_id(user_id) + ' уже в админах'
                    UEngine.reset_privilege()
                else:
                    self.result['message'] = 'Не правильная команда.'
            else:
                self.result['message'] = 'Недостаточно прав.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
