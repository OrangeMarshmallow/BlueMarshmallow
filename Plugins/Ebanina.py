from Plugins.Base import BasePlugin as base
import subprocess


class EbaninaPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Ебанина'
        self.description = 'Считает ебанину для числа'
        self.words = ["ебанина", "ebanina"]

    def func(self):
        try:
            if len(str(self.text)) == 0:
                self.result['message'] = 'Введите число'
                return True
            nums = self.text.split(' ')
            ans = []
            for num in nums:
                _ok = True
                if str(num).isdigit():
                    if int(num) >= 9444732965739290427391:
                        _ok = False
                    if _ok:
                        ans.append(num)
            ans = list(set(ans))
            ans.sort()
            ans_str = ' '.join(ans)
            _res = ''
            if len(ans) > 0:
                _cmd = 'Ebanina.exe ' + ans_str
                _PIPE = subprocess.PIPE
                p = subprocess.Popen(_cmd, shell=True, stdin=_PIPE, stdout=_PIPE, stderr=subprocess.STDOUT,
                                     close_fds=True)

                while True:
                    s = p.stdout.readline()
                    _e = str(s.decode('utf-8'))
                    _e = _e[:-2]
                    _res += _e + '\n'
                    if not s:
                        break
                _res = _res[_res.find('-'):-2]
                lst = _res.split('\n')
                _str = ''
                item = 0
                while item < len(lst) and (len(_str) + len(ans[item]) + len(lst[item]) + 3) <= 4096:
                    _str += ans[item] + ': ' + lst[item] + '\n'
                    item += 1
                if _str != '':
                    self.result['message'] = _str
                else:
                    self.result['message'] = 'Ебаные числа вводишь.'
            else:
                self.result['message'] = 'Ебаные числа вводишь.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
