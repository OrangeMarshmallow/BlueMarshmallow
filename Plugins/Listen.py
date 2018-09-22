from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from VK import VK


class ListenPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Прослушивание'
        self.description = 'Позволяет изменять состояние бота'
        self.words = ["работа", "listen"]
        self.level = 'a'

    def func(self):
        try:
            if self.user == var.czarID:
                if var.listen:
                    VK().Messages().send(message='Завершение работы бота.')
                    var.listen = False
                else:
                    var.listen = True
                    VK().Messages().send(message='Возобновление работы бота.')
            else:
                self.result['message'] = 'Недостаточно прав.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
