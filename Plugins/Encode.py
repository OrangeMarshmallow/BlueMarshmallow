from Plugins.Base import BasePlugin as base
import base64


class EncodePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Шифровальщик'
        self.description = 'Отправляет результат шифрования'
        self.words = ["зашифруй", "encode"]

    def func(self):
        try:
            a = base64.a85encode(str.encode(self.text)).decode('utf-8')
            b = base64.b85encode(str.encode(self.text)).decode('utf-8')
            _code = ''
            for c in range(len(a)):
                _code += a[c] + b[c]
            self.result['message'] = _code
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
