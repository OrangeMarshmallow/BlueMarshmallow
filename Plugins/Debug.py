from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var


class DebugPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Дебаг'
        self.description = 'Режим дебага'
        self.words = ["дебаг", "debug"]
        self.level = 'a'

    def func(self):
        try:
            var.debug_mode = not var.debug_mode
            debug_file = open('DB\\debug.txt', 'w')
            debug_file.write(str({'debug': var.debug_mode}))
            debug_file.close()
            self.result['message'] = f'Режим дебага: {"включен" if var.debug_mode else "выключен"}.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
