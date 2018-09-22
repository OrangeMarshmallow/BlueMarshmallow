from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var


class ExecPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Exec'
        self.description = 'Выводит результат выполнения программы'
        self.words = ["выполни", "exec", "eval", "py"]
        self.level = 'a'

    def func(self):
        try:
            if self.user == var.czarID:
                local = {'result': 'Add "local[\"result\"] = *" to get result'}
                eval(compile(self.text, '<string>', 'exec'))
                self.result['message'] = str(local['result'])
            else:
                self.result['message'] = 'Недостаточно прав'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
