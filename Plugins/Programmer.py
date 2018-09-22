from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from VK import VK
import datetime
import operator
import random


class ProgrammerPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Топ кодеров'
        self.description = 'Определяет кодеров в беседе'
        self.words = ["кодер", "программист", "coder", "programmer"]

    def func(self):
        try:
            f = open('DB\\coder.txt', 'r')
            coder = eval(f.read())
            f.close()
            now = datetime.datetime.now().day
            if coder['today'] == now:
                _str = f'Топ-{len(coder)-1} кодеров этой беседы:\n'
                u = VK().Users().get(user_ids=', '.join([i for i in coder if i != 'today']))
                r = [{(i['first_name'] + ' ' + i['last_name']): coder[str(i['id'])]} for i in u if i != 'id']
                t = str(r)
                t = t.replace('{', '')
                t = t.replace('}', '')
                t = t.replace('[', '')
                t = t.replace(']', '')
                r = eval('{' + t + '}')
                t = sorted(r.items(), key=operator.itemgetter(1))[::-1]
                ind = 1
                for i in t:
                    _str += str(ind) + '. ' + str(i[0]) + ': ' + str(i[1]) + ' раз.\n'
                    ind += 1
                f.close()
                self.result['message'] = _str
            else:
                f = open('DB\\coder.txt', 'w')
                coder['today'] = now
                user = random.choice(VK().Messages().get_chat()['users'])
                if str(user) in coder:
                    coder[str(user)] += 1
                else:
                    coder[str(user)] = 1
                _str = f'В этот раз кодер дня - {UEngine.get_username_by_id(int(user))} (В {coder[str(user)]} раз)'
                f.write(str(coder))
                f.close()
                self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
