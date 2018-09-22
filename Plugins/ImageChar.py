from Plugins.Base import BasePlugin as base
from PIL import Image, ImageDraw, ImageFont
from Utils import Engine as UEngine
from random import randint as ri
import os


class ImageCharPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Символ'
        self.description = 'Отправляет фото символа'
        self.words = ["символ", "char", "symbol"]

    def func(self):
        try:
            msg_id = self.message
            sm = 0
            cnt = 0

            def get_color(n):
                return int(n / 1.25) if sm >= 255 else int(n * 2.5)
            text = self.text

            nums = [int(s) for s in text.split() if s.isdigit()]
            if len(nums) == 3:
                for i in nums:
                    text = text.replace(str(i), '')
            if len(text) > 10:
                text = text[:10]
            tt = text
            text = ''
            for t in tt:
                text += t.upper()
            text = text.replace(' ', '')
            for i in list(text):
                if len(nums) == 3:
                    r, g, b = nums[0], nums[1], nums[2]
                else:
                    r, g, b = ri(0, 255), ri(0, 255), ri(0, 255)
                sm += r + g + b
                image = Image.new('RGB', (500, 500), (r, g, b))
                draw = ImageDraw.Draw(image)
                fnt = ImageFont.truetype('arial.ttf', size=300)
                w, h = fnt.getsize(i)
                draw.text(((500-w)/2, (500-h)/2), i, fill=(get_color(r / 1.4), get_color(g / 1.4), get_color(b / 1.4)),
                          font=fnt)
                image.save(f'ImageChar{msg_id}_{cnt}.jpg', 'JPEG')
                cnt += 1
                del draw
            atts = ''
            for a in range(cnt):
                atts += UEngine.image(f'ImageChar{msg_id}_{a}.jpg') + ','
                os.remove(f'ImageChar{msg_id}_{a}.jpg')
            self.result['attachment'] = atts
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
