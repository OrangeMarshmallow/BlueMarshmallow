from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from VK import VK


class ResetPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Восстановление'
        self.description = 'Восстанавливает фото и название беседы'
        self.words = ["восстановить", "восстанови", "reset"]
        self.level = 'am'

    def func(self):
        try:
            VK().Messages().edit_chat(title=var.title)
            VK().Messages().set_chat_photo(file=var.photo)
            VK().Messages().unpin()
            VK().Messages().pin(message_id=var.pin_id['message_id'])
            self.result['message'] = 'Беседа успешно восстановлена.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
