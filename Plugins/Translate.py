from Plugins.Base import BasePlugin as base
from googletrans import Translator


class TranslatePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Переводчик'
        self.description = 'Переводит текст между с русского на английский и с любого на русский'
        self.words = ["переводчик", "переведи", "перевод", "translate"]

    def func(self):
        try:
            try:
                translator = Translator()
                if len(self.text) > 1:
                    def detect(_text):
                        return str(translator.detect(_text).lang)

                    def translate_function(_text):
                        d = detect(_text)
                        if d == 'ru':
                            return 'ru -> en\n' + _text + ' -> ' + translator.translate(_text, src='ru', dest='en').text
                        else:
                            return d + ' -> ru\n' + _text + ' -> ' + translator.translate(_text, src=d, dest='ru').text

                    self.result['message'] = translate_function(self.text)
                else:
                    self.result['message'] = 'Некорректный текст.'
            except Exception as e:
                self.result['message'] = 'Ошибка: ' + str(e)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
