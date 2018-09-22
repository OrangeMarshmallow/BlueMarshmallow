from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from Utils import Engine as UEngine
from VK import VK


class HistoryPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'История'
        self.description = 'Отправляет статиску сообщений'
        self.words = ["история", "history"]
        self.level = 'am'

    def func(self):
        try:
            count = VK().Messages().get_history(count=0)['count']
            f = open('DB\\history_users.txt', 'r')
            last_static = eval(f.read())
            f.close()
            index = int(last_static['last_static'])
            users = dict()
            if len(last_static) < 2:
                u = VK().Messages().get_chat()['users']
                for i in u:
                    if i != 'last_static':
                        if int(i) > 0:
                            users[str(i)] = 0
            else:
                u = [int(i) for i in last_static if UEngine.is_int(i)]
                users = last_static
            deleted = []
            f = open('DB\\history_cmd.txt', 'r')
            cmd = eval(f.read())
            f.close()
            all_cmd = cmd['last_static']
            var.history_started = False
            while index < count:
                count = VK().Messages().get_history(count=0)['count']
                items = VK().Messages().get_history(count=200, offset=index, rev=1)['items']
                if not var.history_started:
                    _str = f'Подсчет начался.\nЖдите примерно {int((count-index)/300)}~{int((count-index)/225)} секунд.'
                    VK().Messages().send(message=_str)
                    var.history_started = True
                for item in items:
                    if item['from_id'] > 0:
                        if int(item['from_id']) in u:
                            users[str(item['from_id'])] += 1
                        else:
                            deleted.append(int(item['from_id']))
                            u.append(int(item['from_id']))
                            users[str(item['from_id'])] = 1
                        if len(item['body']) > 3:
                            if ' ' in item['body']:
                                msg = item['body'][:item['body'].find(' ')].lower()
                            else:
                                msg = item['body']
                            if msg[0] in '!/\\':
                                all_cmd += 1
                                msg = str(msg[1:]).lower()
                                if msg in var.words:
                                    if msg in cmd:
                                        cmd[str(msg)] += 1
                                    else:
                                        cmd[str(msg)] = 1
                index += 200
            users = dict((x, y) for x, y in [(k, users[k]) for k in sorted(users.keys(), key=users.get, reverse=True)])
            res = f'[{count}] Топ-{len(users)} пользователей этой беседы:\n'
            ind = 1
            # _str = f'Осталось немного, примерно {int((len(users)-1)/4)}~{int((len(users)-1)/3.25)} секунд.'
            # VK().Messages().send(message=_str)
            deleted = VK().Messages().get_chat()['users']
            t = str([int(ii) for ii in ' '.join(users).split() if ii.isdigit()])
            allu = VK().Users().get(user_ids=t[1:len(t)-1])
            for user in users:
                if user != 'last_static':
                    if int(user) > 0:
                        res += f'{ind}. '
                        if not int(user) in deleted:
                            res += '*'
                        un = [(i['first_name'] + ' ' + i['last_name']) for i in allu if int(i['id']) == int(user)][0]
                        res += un + ': ' + str(users[user]) + ' (' + str(round(users[user] / count * 100, 2)) + '%)\n'
                    ind += 1
            cmd = dict((x, y) for x, y in [(k, cmd[k]) for k in sorted(cmd.keys(), key=cmd.get, reverse=True)])
            res_dop = f'[{all_cmd}] Топ-{len(cmd)-1} команд:\n'
            ind = 1
            for c in cmd:
                if c != 'last_static':
                    res_dop += str(ind) + ': ' + str(c) + ': ' + \
                               str(cmd[c]) + '(' + str(round(cmd[c] / all_cmd * 100, 2)) + '%)\n'
                    ind += 1
            users['last_static'] = count
            cmd['last_static'] = all_cmd
            f = open('DB\\history_users.txt', 'w')
            f.write(str(users))
            f.close()
            f = open('DB\\history_cmd.txt', 'w')
            f.write(str(cmd))
            f.close()
            VK().Messages().send(message=res)
            if len(res_dop) >= 4096:
                res_dop = res_dop.split('150')
                VK().Messages().send(message=res_dop[0])
                VK().Messages().send(message='150' + res_dop[1])
            else:
                VK().Messages().send(message=res_dop)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
