from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from PIL import Image, ImageDraw
import requests
import os


class ImageNegativePlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Негатив'
        self.description = 'Отправляет фото в некативе'
        self.words = ["негатив", "negative"]

    def func(self):
        try:
            if not self.photo is None:
                p = requests.get(self.photo)
                out = open('img.jpg', 'wb')
                out.write(p.content)
                out.close()

                image = Image.open('img.jpg')
                draw = ImageDraw.Draw(image)
                width = image.size[0]
                height = image.size[1]
                pix = image.load()

                for i in range(width):
                    for j in range(height):
                        a = pix[i, j][0]
                        b = pix[i, j][1]
                        c = pix[i, j][2]
                        draw.point((i, j), (255 - a, 255 - b, 255 - c))

                image.save('img.jpg', "JPEG")
                del draw
                self.result['attachment'] = UEngine.image('img.jpg')
                os.remove('img.jpg')
            else:
                self.result['message'] = 'Прикрепите фото.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
