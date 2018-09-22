from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import requests
import os


class SiteScreenshot(base):
    def __init__(self):
        super().__init__()
        self.name = 'Скриншот сайта'
        self.description = 'Отправляет скриншот сайта'
        self.words = ["скрин", "screen"]

    def func(self):
        try:
            try:
                p = requests.get('http://api.snapito.io/v2/webshot/spu-ea68c8-ogi2-3cwn3bmfojjlb56e??size=800x0&screen=1024x768&url=' + self.text)
                out = open('img.png', 'wb')
                out.write(p.content)
                out.close()
            except Exception as e:
                self.result['message'] = 'Error: ' + str(e)
            self.result['attachment'] = UEngine.doc('img.png')
            os.remove('img.png')
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
