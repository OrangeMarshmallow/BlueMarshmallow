from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from Settings import BotSettings as var
from operator import xor
from Log import Log
from cmath import *
from Utils.Math import *


class CalculatorPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Калькулятор'
        self.description = 'Отправляет результат вычисления'
        self.words = ["калькулятор", "посчитай", "calc", "calculator"]

    @staticmethod
    def calc(s, m):
        def fib(n):
            return n if n < 2 else (fib(n-1) + fib(n-2))
        from VK import VK
        h = [
            "help",
            "помощь",
            "функции",
            "func",
            "funcs",
            "functions"
        ]
        var.calc_result = None
        s = s.replace('^', '**')
        s = s.replace('«', '<<')
        s = s.replace('÷', '/')
        s = s.replace('×', '*')
        if str(s) in h:
            _str = "Доступно: acos(x), asin(x), atan(x), atan2(x, y), ceil(x), cos(x), cosh(x), degrees(x), rand(x, y)"\
                   "e, exp(x),  fabs(x), floor(x), fmod(x), frexp(x), hypot(x), ldexp(x, y), log(x, base), log10(x), " \
                   "modf(x), pi, pow(x,y), radians(x), sin(x), sinh(x), sqrt(x), tan(x), tanh(x), fib(x), xor(x, y)"
            var.calc_result = _str
            return True
        try:
            safe_dict = {'acos': acos, 'asin': asin, 'atan': atan, 'atan2': atan2, 'ceil': ceil, 'cos': cos,
                         'cosh': cosh, 'degrees': degrees, 'e': e, 'exp': exp, 'fabs': fabs, 'floor': floor,
                         'fmod': fmod, 'frexp': frexp, 'hypot': hypot, 'ldexp': ldexp, 'log': log,
                         'log10': log10, 'modf': modf, 'pi': pi, 'pow': pow, 'radians': radians, 'sin': sin,
                         'sinh': sinh, 'sqrt': sqrt, 'tan': tan, 'tanh': tanh, 'fib': fib, 'xor': xor, 'rand': rand}

            ss = eval(s, {"__builtins__": None}, safe_dict)
            VK().Messages().send(message=str(ss) + '\n' + var.name + ' [' + var.version + ']', forward_messages=m)
            return True
        except Exception as exception:
            var.calc_result = 'Некорректное выражение: ' + str(exception)
            return True

    def func(self):
        try:
            s = self.text.lower()
            m = [
                'backquote',
                'lambda',
                'print',
                'exec',
                'from',
                'import',
                'raise',
                'try',
                'except',
                'finally',
                'import',
                'compile',
                'dir',
                'eval',
                'file',
                'attr',
                'global',
                'hasattr',
                'input',
                'local',
                'open',
                'input',
                'raw',
                'load',
                'vars',
                'set',
                'get',
                'del',
                'class',
                'func',
                'self',
                'code',
                'default',
                'name',
                'tb',
                'frame',
                'next',
                'back',
                'builtin',
                'traceback',
                'exc',
                'type',
                'value',
                '{}',
                '[]',
                'return',
                'data',
                'handl',
                'log',
                'err',
                'use',
                'type',
                'die',
                'rais',
                'as',
                'in',
                '[]',
                '{}',
                '()',
                '[',
                ']',
                '{',
                '}'
                '_',
                ':',
                '=',
                ','
                '"',
                "'",
                'os',
                'path',
                'file',
                'base',
                'name'
            ]
            mn = '1234567890'

            not_safe = ''

            def c(_s, a):
                for i in _s.split():
                    _string = ''
                    for j in i:
                        if j.isalpha():
                            _string += j
                    if _string in a:
                        return True
                return False

            _op = c(s, m)
            n = 0
            for item in s:
                if item in mn:
                    n += 1
            if not n:
                _op = True
            if 'e' in s or 'pi' in s or 'log' in s:
                _op = False

            if not _op:
                tm_sleep = 10

                try:
                    UEngine.timeout(func=CalculatorPlugin().calc,
                                    time=tm_sleep,
                                    exception=f'[{tm_sleep} сек.] Я не смог посчитать.',
                                    args=(str(self.text), self.message, ))
                    if var.calc_result:
                        self.result['message'] = str(var.calc_result)
                except Exception as _e:
                    self.result['message'] = str(_e)
            else:
                self.result['message'] = 'Небезопасное выражение'
                Log.show_info(not_safe)
            return True
        except Exception as _e:
            Log.show_error(_e)
            return False
