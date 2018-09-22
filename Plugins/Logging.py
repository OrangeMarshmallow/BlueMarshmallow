from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var


class LoggingPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Логгирование'
        self.description = 'Настраивает логи'
        self.words = ["лог", "log"]
        self.level = 'a'

    def func(self):
        try:
            words = self.text.split(' ')
            if words[0] == '':
                self.result['message'] = f'Log: {var.log_all}\nText: {var.log_text}\nConsole: {var.log_console}'
            else:
                if words[0] in ['текст', 'text']:
                    var.log_text = not var.log_text
                    self.result['message'] = f'Log.Text = {var.log_text}'
                elif words[0] in ['консоль', 'console']:
                    var.log_console = not var.log_console
                    self.result['message'] = f'Log.Console = {var.log_console}'
                elif words[0] in ['весь', 'all']:
                    var.log_all = not var.log_all
                    self.result['message'] = f'Log.All = {var.log_all}'
                else:
                    self.result['message'] = 'Выберете одно из: текст, консоль, весь'
            log_file = open('DB\\logging.txt', 'w')
            log_file.write(str({'All': var.log_all, 'Text': var.log_text, 'Console': var.log_console}))
            log_file.close()
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
