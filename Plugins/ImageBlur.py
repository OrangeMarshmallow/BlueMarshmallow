from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from PIL import Image, ImageFilter
import requests
import os


class ImageBlurPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Сглаживание'
        self.description = 'Отправляет сглаженное фото'
        self.words = ["сгладь", "сгладить", "блюр", "заблюрь", "blur", "smoothing", "smooth"]

    def func(self):
        try:
            if not self.photo is None:
                if UEngine.is_int(self.text):
                    if 100 >= int(self.text) >= 0:
                        p = requests.get(self.photo)
                        out = open('img.jpg', 'wb')
                        out.write(p.content)
                        out.close()

                        image = Image.open('img.jpg')

                        for i in range(int(self.text)):
                            image = image.filter(ImageFilter.BLUR)

                        image.save('img.jpg', "JPEG")
                        self.result['attachment'] = UEngine.image('img.jpg')
                        os.remove('img.jpg')
                    else:
                        self.result['message'] = 'Введите коэффицент [0..100].'
                else:
                    self.result['message'] = 'Введите коэффицент.'
            else:
                self.result['message'] = 'Прикрепите фото.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
