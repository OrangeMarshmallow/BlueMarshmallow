from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine


class ModerEditPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Редактирование модераторов'
        self.description = 'Позволяет редактировать список модеров'
        self.words = ["модер", "moder"]
        self.level = 'a'

    def func(self):
        try:
            user_id = self.text
            if len(str(user_id)) > 0 and UEngine.user_exist_in_chat(user_id):
                if not int(user_id) in db.moders:
                    if self.mode == '+':
                        db.moders.append(int(user_id))
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' добавлен в модеры'
                    else:
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' не является модером'
                else:
                    if self.mode == '-':
                        db.moders.remove(int(user_id))
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' удален из модеров'
                    else:
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' уже в модерах'
                UEngine.reset_privilege()
            else:
                self.result['message'] = 'Не правильная команда.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
