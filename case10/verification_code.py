#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: verification_code.py
#          Desc: 生成验证码图片
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: http://jase.im/
#       Version: 0.0.1
#    LastChange: 2018-05-15 21:18:37
#       History:
# =============================================================================
'''

from PIL import Image, ImageFont, ImageDraw
import random
import os

class Captcha(object):
    def __init__(self, size=(240,60), fontsize=40):
        self.font = ImageFont.truetype('/Library/Fonts/Arial.ttf', fontsize)
        self.size = size
        self.image = Image.new('RGBA', self.size, (160,160,160,255))
        self.text = self.randText()
        self.color_list = self.randColor()
        self.write()

    def randText(self):
        char_number = 4
        text = ""
        chars = [chr(i) for i in range(65,91)]
        nums = [chr(i) for i in range(48,58)]
        char_and_num = chars + nums
        for i in range(char_number):
            text += "  " + random.choice(char_and_num)
        return text

    def randColor(self):
        color_list = []
        for i in range(3):
            color = ()
            for j in range(4):
                color_temp = (random.randrange(256),)
                color += color_temp
            color_list.append(color)
        return color_list

    def write(self):
        draw = ImageDraw.Draw(self.image)
        draw.text((7,5), self.text, font=self.font, fill=self.color_list[0])
        # draw.text((5,5), self.text, self.font)

    def save(self):
        name = input('File name: ')
        name += '.png'
        path = os.getcwd()
        self.image.save(os.path.join(path, name), 'PNG')


def main():
    imageNew = Captcha()
    imageNew.save()

if __name__ == "__main__":
    main()
