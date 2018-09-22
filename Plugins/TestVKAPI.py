from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from Utils import Engine as UEngine
from VK import VK


class TestVKAPIPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Тест ВК АПИ'
        self.description = 'Позволяет отправлять разные запросы'
        self.words = ["test", "тест"]
        self.level = 'ba'

    def func(self):
        try:
            if self.user == var.czarID:
                try:
                    r = self.text.split(' | ')
                    if len(r) == 2:
                        s = str(VK().exec(r[0], eval(r[1])))
                        s = s[2:len(s) - 2].replace("'", '').split(', ')
                        res = ''
                        for a in s:
                            res += a + '\n'
                        self.result['message'] = res
                    elif len(r) > 2:
                        s = VK().exec(r[0], eval(r[1]))
                        rr1 = ''
                        for i in range(len(r)):
                            if 1 < i < len(r):
                                if UEngine.is_int(r[i]):
                                    s = s[int(r[i])]
                                else:
                                    s = s[r[i]]
                                rr1 += r[i] + ': '
                                print(rr1 + ': ' + s)
                        self.result['message'] = rr1 + str(s).replace("'", '')
                    return True
                except Exception as e:
                    self.result['message'] = 'Error: ' + str(e)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
