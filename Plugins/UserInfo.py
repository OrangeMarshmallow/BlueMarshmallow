from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import codecs


class UserInfoPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Информация о пользователе'
        self.description = 'Говорит инфу о пользователе'
        self.words = ["пользователь", "юзер", "чел", "user"]

    def func(self):
        try:
            f = codecs.open('DB\\userinfo.txt', 'r', 'utf-8')
            t = eval(f.read())
            f.close()
            if self.mode == '+':
                user_id = str(self.user)
                f = codecs.open('DB\\userinfo.txt', 'w', 'utf-8')
                text = self.text
                text = text.replace(': ', ':')
                text = "{'" + text + "'}"
                text = text.replace(':', "':'")
                text = eval(text)
                if str(user_id) in t:
                    for i in text:
                        t[str(user_id)][str(i)] = text[str(i)]
                else:
                    t[str(user_id)] = dict()
                    for i in text:
                        t[str(user_id)][str(i)] = text[str(i)]
                f.write(str(t))
                f.close()
                # r = [t[i] for i in t if i == str(user_id)][0]
                self.result['message'] = 'Добавлено.'
            elif self.mode == '-':
                if str(self.text) in t[str(self.user)]:
                    f = codecs.open('DB\\userinfo.txt', 'w', 'utf-8')
                    t[str(self.user)].pop(str(self.text))
                    f.write(str(t))
                    f.close()
                else:
                    self.result['message'] = 'У вас нет этого поля.'
                self.result['message'] = 'Удалено.'
            else:
                if len(self.text) > 0:
                    user_id = self.text
                else:
                    user_id = str(self.user)
                try:
                    user_id = UEngine.get_user_id(user_id)
                    if str(user_id) in t:
                        r = [t[i] for i in t if i == str(user_id)][0]
                        self.result['message'] = '\n'.join([(i + ': ' + r[i]) for i in r])
                    else:
                        self.result['message'] = 'Пользователь с таким id не заполнил информацию.'
                except Exception as e:
                    self.result['message'] = 'Введите корректный id: ' + str(e)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
