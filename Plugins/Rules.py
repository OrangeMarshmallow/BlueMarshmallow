from Plugins.Base import BasePlugin as base


class RulesPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Правила'
        self.description = 'Выводит правила беседы'
        self.words = ["правила", "rules"]

    def func(self):
        try:
            _str = 'Главное правило - просто не быть уебком.'
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
