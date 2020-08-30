# -*- coding: utf-8 -*-
# !@time: 2020-06-05 05:39
# !@author: superMC @email: 18758266469@163.com
# !@fileName: generate_n_m_dim_array.py

import random


def random_n_md(n, m):
    return [[random.randint(1, n) for j in range(m)] for i in range(n)]
