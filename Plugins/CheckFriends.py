from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from VK import VK


class CheckFriendsPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Подписчики'
        self.description = 'Принимает в друзья всех подписчиков'
        self.words = ["подписчики", "followers"]
        self.level = 'bam'

    def func(self):
        try:
            followers = VK().Users().get_followers()['items']
            users = f'[{len(followers)}] Принятые заявки:\n'
            if len(followers):
                i = 0
                for user in followers:
                    VK().Friends().add(user_id=user)
                    users += str(i+1) + '. ' + UEngine.get_username_by_id(user) + '\n'
                    i += 1
                self.result['message'] = users
            else:
                self.result['message'] = 'Подписчиков не обнаруженно.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
