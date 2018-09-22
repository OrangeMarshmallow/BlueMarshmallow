from Plugins.Base import BasePlugin as base
from gsearch.googlesearch import search


class GooglePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Google'
        self.description = 'Отправляет результаты поиска из гугла'
        self.words = ["гугл", "google"]

    def func(self):
        try:
            num = 1
            n = [int(s) for s in self.text.split() if s.isdigit()]
            t = self.text
            if len(n) > 0:
                num += n[len(n) - 1]
                t = self.text[0:self.text.find(str(num)) - 1]
            _str = t + ':\n'
            i = 0
            results = search(t, num_results=num)
            for result in results:
                res = list(result)
                _str += str(i + 1) + '. ' + res[0] + ': ' + res[1] + '\n'
                i += 1
            self.result['message'] = _str
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
