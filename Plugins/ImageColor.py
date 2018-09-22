from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from PIL import Image, ImageDraw
import requests
import os


class ImageColorPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Цвет изображения'
        self.description = 'Корректирует цвет изображения'
        self.words = ["цвет", "color"]

    def func(self):
        try:
            if self.text.lower() in ['help', 'помощь']:
                self.result['message'] = 'red / green / blue\n' \
                                         'красный / зеленый / синий\n' \
                                         '[r][g][b]'
                return True
            if not self.photo is None:
                if len(self.text.split()):
                    _r = False
                    _g = False
                    _b = False
                    t = self.text.split()
                    if 'red' in t or 'красный' in t or 'r' in t or 'к' in t or \
                            'red' in self.text or 'красный' in self.text:
                        _r = True
                    if 'green' in t or 'зеленый' in t or 'g' in t or 'з' in t or \
                            'green' in self.text or 'зеленый' in self.text or 'зелёный' in t or 'зелёный' in self.text:
                        _g = True
                    if 'blue' in t or 'синий' in t or 'b' in t or 'с' in t or \
                            'blue' in self.text or 'синий' in self.text:
                        _b = True

                    if len(self.text) <= 3 and self.text != 'red':
                        if 'r' in self.text or 'к' in self.text:
                            _r = True
                        if 'g' in self.text or 'з' in self.text:
                            _g = True
                        if 'b' in self.text or 'с' in self.text:
                            _b = True

                    p = requests.get(self.photo)
                    out = open('img.jpg', 'wb')
                    out.write(p.content)
                    out.close()

                    image = Image.open("img.jpg")
                    draw = ImageDraw.Draw(image)
                    width = image.size[0]
                    height = image.size[1]
                    pix = image.load()
                    for i in range(width):
                        for j in range(height):
                            a = pix[i, j][0] * _r
                            b = pix[i, j][1] * _g
                            c = pix[i, j][2] * _b

                            draw.point((i, j), (a, b, c))

                    image.save('img.jpg', "JPEG")
                    del draw
                    self.result['attachment'] = UEngine.image('img.jpg')
                    os.remove('img.jpg')
                else:
                    self.result['message'] = 'Выберите цвет'
            else:
                self.result['message'] = 'Прикрепите фото'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
