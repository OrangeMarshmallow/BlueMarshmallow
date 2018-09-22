from Plugins.Base import BasePlugin as base


class GetInvitePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Приглашение'
        self.description = 'Генерирует ссылку для приглашения пользователей'
        self.words = ["приглашение", "ссылка", "link", "invitelink"]

    def func(self):
        try:
            # self.result['message'] = VK().Messages().get_invite_link()
            self.result['message'] = 'Беседа: https://vk.me/join/AJQ1d5ZY/ATuBzHqo_JVYsp/\n' \
                                     'Бот: https://vk.me/join/AJQ1dxWtGwfiOmT94cs6ju51'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
