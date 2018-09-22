from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine


class WhiteEditPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Редактирование белого списка'
        self.description = 'Позволяет редактировать белый список'
        self.words = ["белый", "white"]
        self.level = 'am'

    def func(self):
        try:
            user_id = self.text
            if len(str(user_id)) > 0:
                if not int(user_id) in db.white:
                    if self.mode == '+':
                        db.white.append(int(user_id))
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' добавлен в белый список'
                    else:
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' не состоит в белом списке'
                else:
                    if self.mode == '-':
                        db.white.remove(int(user_id))
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' удален из белого списка'
                    else:
                        self.result['message'] = UEngine.get_link_by_id(user_id) + ' уже в белом списке'
                UEngine.reset_privilege()
            else:
                self.result['message'] = 'Не правильная команда.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
