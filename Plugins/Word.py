from Plugins.Base import BasePlugin as base
import random


class WordPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Слово'
        self.description = 'Отправляет сгенерированное слово'
        self.words = ["слово", "word"]

    def func(self):
        try:
            a = [
                [
                    "уеыаоэяию",
                    "йцкнгшщзхфвпрлджчсмтб"
                ],
                [
                    "eyuioa",
                    "qwrtpsdfghjklzxcvbnm"
                ]
            ]
            p = False
            q = -1

            aa = [
                "англ",
                "en"
            ]
            bb = [
                "рус",
                "ru"
            ]

            cnt = [int(s) for s in self.text.split() if s.isdigit()][0]
            res = ''
            if cnt > 10:
                cnt = 10
            for i in range(int(cnt)):
                c = ''
                for w in aa:
                    if w in self.text:
                        q = 1
                for w in bb:
                    if w in self.text:
                        q = 0

                if q == -1:
                    q = random.randint(0, 1)
                for w in range(random.randint(3, 10)):
                    if p:
                        c += random.choice(list(a[q][0]))
                        p = False
                    else:
                        c += random.choice(list(a[q][1]))
                        p = True
                res += str(i+1) + ': ' + c + '\n'
            self.result['message'] = res
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
