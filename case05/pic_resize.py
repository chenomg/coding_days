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
from platform import platform
import os
import re


class pic_resize(object):
    """
    Description

    @param param: 脚本目录下pic目录中的图片若长宽尺寸超出最大尺寸则进行缩小，
        不超过的则不变
    @type  param: Type

    @return: Description
    @rtype: Type

    @raise e: Description

    """
    Platform = platform()

    def __init__(
            self,
            # 初始化参数
            # 获取脚本所在目录，并且生成图片所在目录
            path=os.path.join(os.getcwd(), 'pic'),
            max_width=1136,
            max_height=640):
        self.path = path
        self.max_width = max_width
        self.max_height = max_height
        self.image_names_list = []
        self.image_path_name_list = []

    def complete_image_path_name_list_and_names_list(self):
        """
        生成需要进行缩放处理图片的文件名清单和文件完整目录(带文件名)的清单
        """
        image_names_list = []
        image_path_name_list = []
        file_list = os.listdir(self.path)
        for f in file_list:
            if not os.path.isdir(f):
                if re.findall(r'(^(?!thumbnail)).*(\.jp(|e)g|\.png)$', f,
                              re.IGNORECASE):
                    img = Image.open(os.path.join(self.path, f))
                    width, height = img.size
                    if width > self.max_width or height > self.max_height:
                        image_names_list.append(f)
                        image_path_name_list.append(os.path.join(self.path, f))
            else:
                pass
        self.image_path_name_list = image_path_name_list
        self.image_names_list = image_names_list

    def image_zoomout_saver(self):
        """
        根据前面生成的需要处理的文件清单进行缩小处理，
        并在缩小的文件名前面增加thumbnail以区分
        """
        self.complete_image_path_name_list_and_names_list()
        for image in self.image_path_name_list:
            # p = re.compile(r'^\/.+\/')
            p = re.compile(r'.+\\')
            path = p.findall(image)[0]
            path_length = len(path)
            file_name = image[path_length + 1:]
            new_name = 'thumbnail-' + file_name
            output_file = os.path.join(path, new_name)
            img = Image.open(image)
            img.thumbnail((self.max_width, self.max_width))
            img.save(output_file, 'png')
            print("Process done: {}".format(image))


def main():
    work = pic_resize()
    work.image_zoomout_saver()


if __name__ == "__main__":
    main()
