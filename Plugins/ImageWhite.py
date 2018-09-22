from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from PIL import Image, ImageDraw
import requests
import os


class ImageWhitePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Яркость'
        self.description = 'Отправляет фото с яркостью'
        self.words = ["яркость", "bright"]

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
                                a = pix[i, j][0] + factor
                                b = pix[i, j][1] + factor
                                c = pix[i, j][2] + factor
                                if a < 0:
                                    a = 0
                                if b < 0:
                                    b = 0
                                if c < 0:
                                    c = 0
                                if a > 255:
                                    a = 255
                                if b > 255:
                                    b = 255
                                if c > 255:
                                    c = 255
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
