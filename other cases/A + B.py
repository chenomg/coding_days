#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: A + B.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: 给出两个整数a和b, 求他们的和, 但不能使用 + 等数学运算符。
说明:
a和b都是 32位 整数么？

是的
我可以使用位运算符么？

当然可以
"""

aa = 21
bb = 12


def aplusb(a, b):
    c = a ^ b
    d = a & b
    e = c ^ (d << 1)
    f = c & (d << 1)
    if f == 0:
        return c
    return aplusb(e, f)


result = aplusb(aa, bb)
print(result)
