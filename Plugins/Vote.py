from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from Settings import DataBase as db
from Utils import Engine as UEngine
from VK import VK
import time


class VotePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Голосование'
        self.description = 'Запускает голосование'
        self.words = ["голосование", "голос", "vote"]
        self.level = 'am'

    def func(self):
        try:
            vote_time = 60
            _correct = True
            _start = True
            var.getting = True
            if not '?' in self.text or not '!' in self.text:
                _correct = False
            if not _correct:
                if '~' in self.text:
                    _correct = True
            command = ''
            if _correct:
                _id = 0
                q = ''
                a = []
                _users_voted = []
                _messages_voted = []
                _cmd_active = False
                if '~' in self.text:
                    command = self.text[1:self.text.find(' ')]
                    mes = self.text[self.text.find(' ') + 1:]
                    a.append(['Да', 0])
                    a.append(['Нет', 0])
                    try:
                        mes = UEngine.get_user_id(mes)
                        _id = int(mes)
                        if _id in db.privilege or _id in db.white or not UEngine.user_exist_in_chat(_id):
                            _start = False
                        mes = UEngine.get_link_by_id(_id)
                        _cmd_active = True
                    except Exception as _exc:
                        print(_exc)
                        _start = False
                else:
                    q = self.text[:self.text.find('?')]
                    mes = self.text[self.text.find('?') + 2:]
                if not _cmd_active:
                    while mes != '':
                        a.append([mes[:mes.find('!')], 0])
                        mes = mes[mes.find('!') + 2:]

                def get():
                    _all_votes = 0
                    _start_in = VK().Messages().get_history(count=0)['count']
                    time.sleep(vote_time)
                    _end = VK().Messages().get_history(count=0)['count']
                    cnt = (_end - _start_in) * 2
                    response = VK().Messages().get_history(count=cnt)['items']
                    response = response[::-1]
                    for item in response:
                        _a = item['body'].lower()
                        i = 0
                        _in = True
                        if not item['user_id'] in _users_voted and not '?' in _a:
                            while i < len(a) and _in:
                                if a[i][0].lower() == _a:
                                    a[i][1] += 1
                                    _all_votes += 1
                                    _in = False
                                i += 1
                            if not _in:
                                _users_voted.append(item['user_id'])
                                _messages_voted.append(item['id'])
                    _str = 'Результаты:\n'
                    i = 0

                    def f(n, c):
                        _f = 100 / n * c
                        if c == 0:
                            return '0.00'
                        else:
                            return str(int(_f * 100) / 100)

                    def sort_col(n):
                        return n[1]

                    if _all_votes > 0:
                        a.sort(key=sort_col, reverse=True)

                        while i < len(a):
                            _str += str(a[i][1]) + '. ' + a[i][0] + ' [%' + f(_all_votes, a[i][1]) + ']\n'
                            i += 1
                        VK().Messages().send(message=_str,
                                             forward_messages=', '.join(str(_exc_in) for _exc_in in _messages_voted))
                        if command:
                            if a[0][1] == a[1][1]:
                                self.result['message'] = 'Живи' + self.text
                            elif a[0][0] == 'Да':
                                VK().Messages().remove_chat_user(user_id=_id)
                            else:
                                self.result['message'] = 'Живи' + self.text
                        return True
                    else:
                        self.result['message'] = 'Голосование отменено.'

                def start(question=None, answers=None):
                    _str = f'[{vote_time} sec] Голосование: '
                    if command != '':
                        _str += command + ' -> ' + mes
                    else:
                        _str += question
                    _str += '\n'
                    _i = 1
                    for i in answers:
                        _str += '- ' + i[0] + '\n'
                        _i += 1
                    VK().Messages().send(message=_str)
                    get()

                if _start:
                    start(q, a)
                else:
                    self.result['message'] = 'Ошибка'
            else:
                self.result['message'] = 'Неправильная команда'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
