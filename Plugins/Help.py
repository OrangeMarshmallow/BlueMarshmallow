from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
import os
import io


class HelpPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Помощь'
        self.description = 'Выводит общую информацию о беседе'
        self.words = ["помощь", "хелп", "хелпа", "help"]

    def func(self):
            lines = 0
            chars = 0
            words = 0

            tree = os.walk(os.getcwd())
            for dirs in tree:
                s = dirs[0]
                if not '__' in s and not 'idea' in s and not '.' in s:
                    for fname in os.listdir(s):
                        if '.py' in fname and not 'pyc' in fname and not '__' in fname:
                            fn = s + '\\' + fname
                            file = io.open(fn, encoding='utf-8', errors='ignore')
                            for line in file:
                                words += len(line.split())
                                lines += 1
                                chars += len(line)

            _str = f"Данная беседа находится под управлением {var.name} [v{var.version}]\n"
            _str += "Кодер бота является представителем GeekHub.PRO\n"
            _str += "Чтобы узнать список плагинов, напишите !плагины\n"
            _str += "Чтобы узнать информацию о плагине, введите !?плагин\n"
            _str += "Чтобы узнать администраторов беседы, напишите !админы\n"
            _str += "Чтобы узнать правила беседы, напишите !правила\n"
            _str += "Чтобы узнать информацию о пользователе, введите !юзер *id*\n"
            _str += "Чтобы узнать кто знает какой ЯП, введите !яп\n"
            _str += f"\nВ боте:\n~ {len(var.plugins)} плагинов\n~ {lines} строк\n~ {words} слов\n~ {chars} символов"
            self.result['message'] = _str
            return True
