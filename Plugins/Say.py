from Plugins.Base import BasePlugin as base


class SayPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Скажи'
        self.description = 'Бот говорит то, что ему скажут'
        self.words = ["скажи", "повтори", "say", "repeat"]

    def func(self):
        try:
            self.result['message'] = self.text
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
