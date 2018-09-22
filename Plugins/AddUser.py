from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine
from Log import Log
from VK import VK


class AddUserPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Добавление человека'
        self.description = 'Позволяет добавлять человека в беседу'
        self.words = ["добавить", "добавь", "пригласить", "пригласи", "инвайт", "invite", "add"]
        self.level = 'a'

    def func(self):
        try:
            user_id = self.text
            if 'id' in user_id:
                user_id = user_id[2:len(user_id)]
            if not int(user_id) in db.black:
                if UEngine.user_exist_in_chat(user_id):
                    self.result['message'] = 'Этот пользователь уже в беседе'
                elif not UEngine.user_exist_in_friends(user_id):
                    self.result['message'] = 'Этот пользователь должен быть у меня в друзьях'
                else:
                    VK().Messages().add_chat_user(user_id=user_id)
                    self.result['message'] = UEngine.get_username_by_id(user_id=user_id) + ' приглашен.'
                Log.show_info(str(UEngine.get_username_by_id(UEngine.get_user_id_by_message(self.message))) +
                              'пытался пригласить ' + UEngine.get_username_by_id(user_id))
            else:
                self.result['message'] = 'Этот пользователь находится в чс.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
