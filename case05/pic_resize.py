#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: pic_resize.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5(1136*640) 分辨率的大小。
"""

from PIL import Image
import os
import re


def image_path_list(path):
    image_name_list = []
    image_path_list = []
    file_list = os.listdir(path)
    for f in file_list:
        if not os.path.isdir(f):
            if re.findall(r'(\.jp(|e)g|\.png)$', f, re.IGNORECASE):
                image_name_list.append(f)
                image_path_list.append(os.path.join(path, f))
        else:
            pass
    return image_path_list


def image_zoomout(image, max_width, max_height):
    path = re.findall(r'^\/.+\/', image)
    file_name = re.findall(r'\w+\.\w+$', image)
    new_name = 'thumbnail-' + file_name
    output_file = os.path.join(path, new_name)
    img = Image.open(image)
    width, height = img.size
    if width > 1136 or height > 640:
        if width / height > 1136 / 640:
            rate = width / 1136
            img.thumbnail(width / rate, height / rate)
            img.save(new_name, 'jpeg')
        else:
            rate = height / 640
            img.thumbnail(width / rate, height / rate)
            img.save(new_name, 'jpeg')


def main():
    addr = '/Users/chenomg/code/coding_days/case05/pic/'
    image_files = []
    # files = file_list(addr)
    image_files = image_path_list(addr)
    print(image_files)
    # image = Image.open(image_files[0])
    # image.show()
    path = re.findall(r'^\/.+\/', image_files[0])
    print(image_files[0])
    print(path)


if __name__ == "__main__":
    main()
