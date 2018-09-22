from Plugins.Base import BasePlugin as base
from Settings import DataBase as db
from Utils import Engine as UEngine
from Log import Log
from VK import VK


class DeleteUserPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Удаление человека'
        self.description = 'Позволяет удалять человека из беседы'
        self.words = ["удалить", "удали", "кик", "кикни", "kick"]
        self.level = 'a'

    def func(self):
        try:
            user_id = self.text
            if 'id' in str(user_id):
                user_id = user_id[2:len(user_id)]
            else:
                user_id = UEngine.get_user_id(user_id)
            if int(user_id) in db.privilege:
                self.result['message'] = 'Нельзя кикнуть привилегированного.'
            elif UEngine.user_exist_in_chat(user_id):
                VK().Messages().remove_chat_user(user_id=user_id)
                self.result['message'] = UEngine.get_username_by_id(user_id) + ' кикнут.'
            else:
                self.result['message'] = 'Такого пользователя нет в беседе.'
            Log.show_info(str(UEngine.get_username_by_id(UEngine.get_user_id_by_message(self.message))) +
                          'пытался кикнуть ' + UEngine.get_username_by_id(user_id))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
