# -*- coding: utf-8 -*-
# !@time: 2020/10/9 6:14 下午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 2.py
"""两个有序数组的公共元素"""


def get_common_element(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a == 0 or len_b == 0:
        return []

    ret = []
    i = 0
    j = 0
    while i != len_a and j != len_b:
        if a[i] == b[j]:
            ret.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    return ret


a = [1, 2, 3, 6, 7, 9, 12, 13, 20]
b = [3, 6, 9, 12, 15, 18, 21]
c = get_common_element(a, b)
print(c)
