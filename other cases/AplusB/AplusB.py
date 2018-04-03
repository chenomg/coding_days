#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: AplusB.py
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


class Solution(object):
    def aplusb(self, a, b):
        if a >= 0 and b >=0:
            c = a ^ b
            d = (a & b) << 1
            if d == 0:
                return c
            return self.aplusb(c, d)
        elif a < 0 and b >= 0:
            minus_a = self.aplusb(~a, 1)
            c = self.aplusb(minus_a, b)
            return c
        elif b < 0 and a >= 0:
            minus_b = self.aplusb(~b, 1)
            c = self.aplusb(minus_b, a)
            return c

    def main(self):
        a_int = 121
        b_int = 82
        result_value = self.aplusb(a_int, b_int)
        print(result_value)


if __name__ == "__main__":
    solution = Solution()
    solution.main()
