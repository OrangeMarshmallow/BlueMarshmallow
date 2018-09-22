from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from Utils import Engine as UEngine
import codecs


class NotePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Записка'
        self.description = 'В определенный день напомнит то, что вы попросите'
        self.words = ["записка", "напомни", "note"]

    def func(self):
        try:
            f = codecs.open('DB\\note.txt', 'r', 'utf-8')
            t = eval(f.read())
            f.close()
            if len(str(self.text)) > 0:
                if self.mode == '+':
                    t.append({str(UEngine.get_username_by_id(self.user)): str(self.text)})
                    f = codecs.open('DB\\note.txt', 'w', 'utf-8')
                    var.opened_bd = True
                    f.write(str(t))
                    f.close()
                    self.result['message'] = 'Записка добавлена.'
            else:
                self.result['message'] = '\n'.join([[(j + ': ' + i[j]) for j in i][0] for i in t])
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
