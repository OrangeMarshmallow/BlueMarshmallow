from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from VK import VK
import codecs


class ReputationPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Репутация'
        self.description = 'Управление репутацией'
        self.words = ["репутация", "реп", "reputation", "rep"]

    def func(self):
        try:
            f = codecs.open('DB\\rep.txt', 'r', 'utf-8')
            t = eval(f.read())
            f.close()
            users = VK().Messages().get_chat()['users']
            if len(str(self.text)) > 0:
                try:
                    user = UEngine.get_username_by_id(str(self.text))
                    try:
                        user_id = UEngine.get_user_id(str(self.text))
                    except Exception as e:
                        self.result['message'] = 'Пользователя с таким id нет: ' + str(e)
                        return True
                    if str(user_id) == str(self.user):
                        self.result['message'] = 'Ди нахуй)'
                        return True
                    if int(user_id) in users:
                        if self.mode == '+':
                            f = codecs.open('DB\\rep.txt', 'w', 'utf-8')
                            if user in t:
                                t[user].append(UEngine.get_username_by_id(self.user))
                            else:
                                t[user] = [UEngine.get_username_by_id(self.user)]
                            self.result['message'] = 'Репутация добавлена'
                            f.write(str(t))
                            f.close()
                        elif self.mode == '-':
                            if user in t:
                                f = codecs.open('DB\\rep.txt', 'w', 'utf-8')
                                t[user].remove(UEngine.get_username_by_id(self.user))
                                f.write(str(t))
                                f.close()
                                self.result['message'] = 'Репутация удалена'
                            else:
                                self.result['message'] = 'Вы не давали ему репутацию.'
                    else:
                        self.result['message'] = 'Пользователя с таким id нет в беседе.'
                except Exception as e:
                    self.result['message'] = 'Введите корректный id: ' + str(e)
            else:
                s = [i for i in t]
                self.result['message'] = '\n'.join([(i + ' (' + str(len(t[i])) + '): ' + ', '.join(t[i])) for i in s])
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
