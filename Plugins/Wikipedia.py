from Plugins.Base import BasePlugin as base
import wikipedia


class WikipediaPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Википедия'
        self.description = 'Отправляет информацию о чем-либо'
        self.words = ["википедия", "вики", "wiki", "wikipedia"]

    def func(self):
        text = self.text
        try:
            if text == '':
                self.result['message'] = 'Некорректный запрос'
            else:
                _str = ''
                try:
                    wikipedia.set_lang('ru')
                    s = wikipedia.page(text)
                    t = s.title
                    c = s.content
                    c = c[0:c.find('==') - 3]
                    _str += f'{t}:\n'
                    _str += c
                    self.result['message'] = _str
                except Exception as _e:
                    _e = str(_e)
                    _e = _e[_e.find(':') + 3:len(_e)]
                    _str += 'Слишком много вариантов:\n' + _e
                    self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
