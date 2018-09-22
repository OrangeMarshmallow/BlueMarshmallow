from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine


class ReportPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Жалоба'
        self.description = 'Позволяет пожаловаться на сообщение'
        self.words = ["жалоба", "report"]
        self.level = 'amu'

    def func(self):
        try:
            message = UEngine.get_message_by_id(self.message)
            if 'fwd_messages' in message['items'][0]:
                _str = UEngine.get_username_by_id(message['items'][0]['user_id']) + ' пожаловался на ' + \
                       UEngine.get_username_by_id(message['items'][0]['fwd_messages'][0]['user_id']) + ': "' + \
                       message['items'][0]['fwd_messages'][0]['body'] + '"'
                # Log.show_info(_str)
                f = open('DB\\report.txt', 'a')
                f.write(_str + '\n')
                f.close()
                self.result['message'] = f'Report for ' \
                                         f'{UEngine.get_link_by_id(message["items"][0]["fwd_messages"][0]["user_id"])}'\
                                         f' submitted, report id {message["items"][0]["id"] * 1177647263131337}.'
            else:
                self.result['message'] = 'Пожаловаться можно только на сообщение'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
