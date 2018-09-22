from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from PIL import Image, ImageDraw
import requests
import os


class ImageMirrorPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Отзеркаливание'
        self.description = 'Отправляет зеркальное фото'
        self.words = ["зеркало", "отзеркаль", "mirror"]

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

                part1 = image.crop((0, 0, width / 2, height))
                part2 = part1.transpose(Image.FLIP_LEFT_RIGHT)
                image.paste(part2, (round(width / 2), 0))

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
