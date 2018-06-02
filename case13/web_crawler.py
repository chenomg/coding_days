#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: web_crawler.py
#          Desc: 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
#                http://tieba.baidu.com/p/5728621205
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-06-01 22:28:37
#       History:
# =============================================================================
'''

import requests
import re
from lxml import html
import os


class Image_Downloader(object):
    def __init__(self, url=None):
        self.url = url

    def get_image_links(self):
        # 图片地址
        img_list = []
        headers = {
            'user-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        r = requests.get(self.url, headers=headers)
        selector = html.fromstring(r.text)
        for sel in selector.xpath(
                '//div[starts-with(@class, "d_post_content j_d_post_content")]'
        ):
            for img in sel.xpath("img/@src"):
                img_list.append(img)
        return img_list

    def download_img(self, img_urls, path=os.getcwd()):
        # 首先检查是否有图片
        if not img_urls:
            print('Image not found!')
        else:
            for img in img_urls:
                # 图片保存名字
                file_name = re.findall(r'\/([\d\w]+\.jpg)', img)
                if file_name:
                    # 二进制写入图片
                    with open(os.path.join(path, file_name[0]), 'wb') as f:
                        f.write(requests.get(img).content)
            print('Download done...')

    def get_large_image_links(self):
        pass

    def next_link(self):
        pass


def main():
    url = 'http://tieba.baidu.com/p/2166231880'
    # 在当前目录下请先创建image文件夹
    path = 'image'
    crawler = Image_Downloader(url)
    img_urls = crawler.get_image_links()
    crawler.download_img(img_urls, path=path)


if __name__ == "__main__":
    main()
