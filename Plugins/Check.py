from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from Settings import DataBase as db
from Utils import Engine as UEngine
from VK import VK


class CheckPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Проверка'
        self.description = 'Проверка на редактирование беседы'
        self.words = ["проверь", "проверка", "check"]
        self.level = 'bam'

    def func(self):
        try:
            err = 0
            history = VK().Messages().get_history(count=10, offset=10)['items']
            for item in history:
                if 'action' in item:
                    if item['action'] == 'chat_title_update':
                        VK().Messages().edit_chat(title=var.title)
                        err += 1
                    if item['action'] == 'chat_photo_update':
                        VK().Messages().set_chat_photo(file=var.photo)
                        err += 1
                    if item['action'] == 'chat_invite_user_by_link':
                        if not int(item['action_mid']) in db.black:
                            VK().Messages().send(message='Добро пожаловать, ' +
                                                         UEngine.get_link_by_id(item['action_mid']) + '.')
                        else:
                            VK().Messages().remove_chat_user(user_id=item['action_mid'])
                    if item['action'] == 'chat_invite_user' or item['action'] == 'chat_kick_user':
                        if not int(item['from_id']) in db.privilege:
                            VK().Messages().remove_chat_user(user_id=item['from_id'])
                            if int(item['from_id']) != int(item['action_mid']):
                                VK().Messages().remove_chat_user(user_id=item['action_mid'])
                            err += 1
                        response = VK().Messages().get_chat()['users']
                        for user in response:
                            if int(user) in db.black:
                                VK().Messages().remove_chat_user(user_id=user)
                                err += 1
            chat_title = VK().Messages().get_chat()['title']
            if chat_title != var.title:
                VK().Messages().edit_chat(title=var.title)
                err += 1
            if err == 0:
                VK().Messages().send(message='Нарушений не обнаруженно.')
            if err > 0:
                VK().Messages().send(message='Я как всегда на страже этой беседы.')
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
