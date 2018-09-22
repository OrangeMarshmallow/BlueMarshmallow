from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import codecs


class LanguagesPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'ЯПы'
        self.description = 'Показывает список пользователей, которые владеют каким-то ЯПом'
        self.words = ["яп", "кодеры"]

    def func(self):
        try:
            f = codecs.open('DB\\languages.txt', 'r', 'utf-8')
            t = eval(f.read())
            f.close()
            if self.mode == '+':
                if str(self.text) in t:
                    u = str(UEngine.get_username_by_id(self.user))
                    if not u in t[str(self.text)]:
                        f = codecs.open('DB\\languages.txt', 'w', 'utf-8')
                        t[str(self.text)].append(u)
                        f.write(str(t))
                        f.close()
                        self.result['message'] = f'Теперь {u} знает {str(self.text)}'
                    else:
                        self.result['message'] = 'Уже есть.'
                else:
                    self.result['message'] = f'Введите корректный ЯП: ' + ', '.join([i for i in t])
            elif self.mode == '-':
                if str(self.text) in t:
                    u = str(UEngine.get_username_by_id(self.user))
                    if u in t[str(self.text)]:
                        f = codecs.open('DB\\languages.txt', 'w', 'utf-8')
                        t[str(self.text)].remove(u)
                        f.write(str(t))
                        f.close()
                        self.result['message'] = f'Теперь {u} не знает {str(self.text)}'
                    else:
                        self.result['message'] = 'Ты не знаешь этот язык.'
            else:
                if str(self.text) in t:
                    self.result['message'] = ', '.join(t[str(self.text)])
                else:
                    s = [i for i in t]
                    self.result['message'] = '\n'.join([(i + ': ' + ', '.join(t[i])) for i in s])
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
