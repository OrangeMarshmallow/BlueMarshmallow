from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
import matplotlib.pyplot as plt
from Utils.Math import *
from cmath import *
import numpy as np
import imageio
import os


class ImageFractalPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Фрактал'
        self.description = 'Отправляет фрактальное изображение'
        self.words = ["фрактал", "fractal"]
        # self.hide = True
        # self.job = False

    def func(self):
        try:
            self.text = self.text.replace('^', '**')

            def mandelbrot(s, pmin, pmax, ppoints, qmin, qmax, qpoints, max_iterations=200, infinity_border=10):
                image = np.zeros((ppoints, qpoints))
                p, q = np.mgrid[pmin:pmax:(ppoints * 1j), qmin:qmax:(qpoints * 1j)]
                c = p + 1j * q
                z = np.zeros_like(c)
                for k in range(max_iterations):
                    z = eval(s)
                    mask = (np.abs(z) > infinity_border) & (image == 0)
                    image[mask] = k
                    z[mask] = np.nan
                    plt.imsave(fname=f'img{k}.jpg', arr=-image.T, cmap='flag')
                return -image.T

            if len(self.text) == 0:
                self.text = 'z**2 + c'
            if not 'c' in self.text:
                self.text += ' + c'
            if not 'z' in self.text:
                self.text = 'z * ' + self.text

            plt.figure(figsize=(10, 10))
            mandelbrot(self.text, -2.5, 1.5, 500, -2, 2, 500, 100)
            plt.xticks([])
            plt.yticks([])

            if self.mode == '+':
                images = []
                for img in range(0, 100):
                    imgname = 'img' + str(img) + '.jpg'
                    images.append(imageio.imread(imgname))
                imageio.mimsave('img.gif', images)

            for i in range(0, 99):
                os.remove(f'img{i}.jpg')

            if self.mode == '+':
                self.result['attachment'] = UEngine.doc('img.gif')
                os.remove('img.gif')
            else:
                self.result['attachment'] = UEngine.image('img99.jpg')
                os.remove('img99.jpg')
            return True
        except Exception as _e:
            self.result['message'] = str(_e)
        return False
