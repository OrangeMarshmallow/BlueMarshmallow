from Plugins.Base import BasePlugin as base
import base64


class DecodePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Расшифровальщик'
        self.description = 'Отправляет результат расшифрования'
        self.words = ["расшифруй", "decode"]

    def func(self):
        try:
            index = 0
            _code_a = ''
            _code_b = ''
            _de_a = ''
            _de_b = ''
            while index < len(self.text):
                _code_a += self.text[index]
                index += 2
            index = 1
            while index < len(self.text):
                _code_b += self.text[index]
                index += 2
            try:
                _de_a += base64.a85decode(str.encode(_code_a)).decode('utf-8')
                _de_b += base64.b85decode(str.encode(_code_b)).decode('utf-8')
            except Exception as exc:
                print(exc)
                self.result['message'] = 'Строка повреждена'
                return True
            if _de_a == _de_b and _de_a != '':
                self.result['message'] = _de_a
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
