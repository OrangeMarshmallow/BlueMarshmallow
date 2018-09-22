from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var


class BotOnlinePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Онлайн бота'
        self.description = 'Позволяет устанавливать онлайн\\оффлайн бота'
        self.words = ["ботонлайн", "botonline"]
        self.level = 'am'

    def func(self):
        try:
            if var.bot_online:
                var.bot_online = False
                self.result['message'] = 'Я теперь оффлайн'
            else:
                var.bot_online = True
                self.result['message'] = 'Я теперь онлайн'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
