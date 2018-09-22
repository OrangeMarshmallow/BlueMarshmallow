from Utils import Engine as UEngine
from Settings import BotSettings as var


class BasePlugin(object):
    def __init__(self):
        self.name = 'name'
        self.description = 'description'
        self.words = ['word']
        self.mode = ''
        self.text = ''
        self.photo = ''
        self.result = {'message': '', 'attachment': None, 'lat': None, 'long': None,
                       'forward_messages': None, 'plugin': None}
        self.level = 'bamu'
        self.message = None
        self.ulvl = None
        self.user = None
        self.hide = False
        self.job = True
        self.debug = False

    def run(self):
        self.result['plugin'] = self.name
        if self.mode == '?':
            self.get_info()
        else:
            self.func()
        return self.result

    def cmd(self, text, photo, user, mode, message_id):
        self.message = message_id
        self.result['message'] = ''
        self.result['attachment'] = ''
        self.user = user
        self.photo = photo
        self.text = str.encode(text).decode('utf-8')
        if text[0] == '?':
            self.mode = '?'
            text = text[1:len(text)]
        elif text[0] == '-':
            self.mode = '-'
            text = text[1:len(text)]
        elif text[0] == '+':
            self.mode = '+'
            text = text[1:len(text)]
        else:
            self.mode = 'None'
        helping = ''
        if ' ' in text:
            helping = text[text.find(' ')+1:len(text)]
            text = text[0:text.find(' ')]
        if text.lower() in self.words:
            if self.job or self.debug:
                if not self.debug:
                    if mode in self.level:
                        self.ulvl = mode
                        self.text = helping
                        return self.run()
                    else:
                        var.start_now = True
                        UEngine.non()
                        return False
                else:
                    if mode == 'a':
                        self.ulvl = mode
                        self.text = helping
                        return self.run()
                    else:
                        var.start_now = True
                        UEngine.debug()
                        return False
            else:
                UEngine.job()
        return False

    def func(self):
        self.result = self.text
        pass

    def get_info(self):
        self.result['message'] = 'Название плагина: ' + self.name + \
                                 '\nОписание: ' + self.description + \
                                 '\nКоманды: ' + ', '.join(self.words)
