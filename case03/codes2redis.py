#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
from functools import wraps
import sys
sys.path.append('..')
from case01.gene_activation_code import Gene_activation_codes

# 如果设置了密码，就加上password=密码
r = redis.Redis()
# 实例化激活码生成器
gene = Gene_activation_codes()
for i in range(1, 201):
    code = gene.gene_a_code(length=12)
    print(code)
    r.set(i, code)
print('dbsize: %s' % r.dbsize())
print(r.keys())
