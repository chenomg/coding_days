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

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
import os


class Captcha(object):
    """生成验证码

    @param size, fontsize: 验证码图片大小，字体大小
    @type  size, fontsize: tuple, int

    @return: 保存图片
    @rtype : png

    @raise e: None
    """

    def __init__(self, size=(240, 60), fontsize=45):
        # 设置文本字体
        self.font = ImageFont.truetype('/Library/Fonts/Arial.ttf', fontsize)
        # 验证码图片大小
        self.size = size
        # 生成空白的新图片
        self.image = Image.new('RGBA', self.size)
        # 随机填充背景
        self.randImgPoint()
        # 生成写入文本
        self.text_list = self.randText()
        # 生成文本写入的颜色
        self.color_list = self.randColor()
        # 将文字写入图像
        self.write()
        # 记录验证码值
        self.value = "".join(self.text_list)

    def randImgPoint(self):
        # 随机填充验证码背景
        draw = ImageDraw.Draw(self.image)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                draw.point((i, j), fill=self.randColor()[0])

    def randText(self):
        # 生成需要写入图像的文字
        char_number = 4
        text = []
        # 大写字母列表
        chars = [chr(i) for i in range(65, 91)]
        # 数值列表
        nums = [chr(i) for i in range(48, 58)]
        # 字母+数值列表
        char_and_num = chars + nums
        for i in range(char_number):
            text.append(random.choice(char_and_num))
        return text

    def randColor(self):
        # 生成四个文字的颜色
        color_list = []
        for i in range(4):
            # 一种颜色存储在一个tuple中
            color = ()
            for j in range(4):
                color_temp = (random.randrange(256), )
                color += color_temp
            # 列表：四个颜色值
            color_list.append(color)
        return color_list

    def write(self):
        # 将文字根据颜色值写入图像
        draw = ImageDraw.Draw(self.image)
        # 文字写入的起始位置
        x, y = random.randrange(35, 70), 5
        for i in range(len(self.text_list)):
            draw.text(
                (x, y),
                self.text_list[i],
                font=self.font,
                fill=self.color_list[i])
            # 使写入的文字间距随机化
            x += random.randrange(30, 50)
        # 给图像添加滤镜
        self.img_filter = self.image.filter(ImageFilter.BoxBlur(1))

    def save(self, filename=None, path=os.getcwd()):
        # 保存验证码到png文件
        # 默认以验证码作为图片名称,也可指定保存的名字
        if not filename:
            filename = self.value
        try:
            if not os.path.isdir(path):
                os.makedirs(path)
            filename += '.png'
            # 默认保存到当前目录下, 亦可保存到指定的验证码文件夹
            self.img_filter.save(os.path.join(path, filename), 'PNG')
        except OSError as err:
            print(str(err))


def main():
    imageCer = Captcha()
    # 以验证码值为名保存到当前目录的验证码文件夹下
    imageCer.save(path='验证码')
    print("验证码：" + imageCer.value)


if __name__ == "__main__":
    main()
