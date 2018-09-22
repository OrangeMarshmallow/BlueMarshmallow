from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from PIL import Image, ImageDraw
import requests
import os


class ImageBlackWhitePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Черно-белое фото'
        self.description = 'Отправляет черно-белый вариант фото'
        self.words = ["чернобелый", "blackwhite"]

    def func(self):
        try:
            if not self.photo is None:
                if UEngine.is_int(self.text):
                    if 100 >= int(self.text) >= -100:
                        p = requests.get(self.photo)
                        out = open('img.jpg', 'wb')
                        out.write(p.content)
                        out.close()

                        image = Image.open('img.jpg')
                        draw = ImageDraw.Draw(image)
                        width = image.size[0]
                        height = image.size[1]
                        pix = image.load()

                        factor = int(self.text)
                        for i in range(width):
                            for j in range(height):
                                a = pix[i, j][0]
                                b = pix[i, j][1]
                                c = pix[i, j][2]
                                s = a + b + c
                                if s > (((255 + factor) // 2) * 3):
                                    a, b, c = 255, 255, 255
                                else:
                                    a, b, c = 0, 0, 0
                                draw.point((i, j), (a, b, c))

                        image.save('img.jpg', "JPEG")
                        del draw
                        self.result['attachment'] = UEngine.image('img.jpg')
                        os.remove('img.jpg')
                    else:
                        self.result['message'] = 'Введите коэффицент [-100..100].'
                else:
                    self.result['message'] = 'Введите коэффицент.'
            else:
                self.result['message'] = 'Прикрепите фото.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
