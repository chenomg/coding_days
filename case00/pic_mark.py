#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class PicMark(object):
    def __init__(self, origin_name=None, mark='1'):
        self.origin_name = origin_name
        self.modified_name = 'modified_' + origin_name
        self.mark = mark

    def picmarkProcess(self):
        image = Image.open(self.origin_name)
        draw = ImageDraw.Draw(image)
        width, height = image.size
        fontSize = int(width * 0.17)
        # print('width: %s, height: %s, fontSize: %s.' % (width, height, fontSize))
        fillColor = "#ff0000"
        # # Windows 字体
        # setFont = ImageFont.truetype('C:/Windows/Fonts/msyh.ttf', fontSize)
        # Mac 字体
        setFont = ImageFont.truetype('/Library/Fonts/Microsoft Sans Serif.ttf', fontSize)
        draw.text(
            (0.8 * width, 0.1 * height),
            self.mark,
            font=setFont,
            fill=fillColor)
        image.save(self.modified_name)


if __name__ == "__main__":
    pp = PicMark('origin.jpg', )
    pp.picmarkProcess()
