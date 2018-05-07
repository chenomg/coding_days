#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: html_href.py
#          Desc:
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: http://jase.im/
#       Version: 0.0.1
#    LastChange: 2018-05-07 21:40:19
#       History:
# =============================================================================
'''

from lxml import html
import requests
import re

file_name = 'links_.txt'
url = "http://www.sina.com.cn/"
headers = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
response = requests.get(url, headers=headers)
selector = html.fromstring(response.text)
with open(file_name, 'w') as f:
    # 获取网页中的所有链接
    for sel in selector.xpath(r"//a/@href"):
        # 所有链接中筛选出所需要的链接
        if re.findall('^http(s)?\:', sel):
            # 结果保存到文件
            f.write(sel.strip() + '\n')
