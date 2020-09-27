# -*- coding: utf-8 -*-
# !@time: 2020/8/21 7:41 下午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1.py

def findout(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    # 字符串求交集
    s = str1 & str2
    return len(s)


def func(line1, line2, n):
    pre1 = line1[: line1.index('x')]
    behind1 = line1[line1.index('x') + 1:]

    pre2 = line2[: line2.index('x')]
    behind2 = line2[line2.index('x') + 1:]
    return findout(pre1, pre2) + 1, n - findout(behind1, behind2)


if __name__ == '__main__':
    n = 10
    line1 = ['a', 'b', 'c', 'd', 'e', 'x', 'f', 'h', 'i', 'j']
    line2 = ['a', 'c', 'i', 'x', 'e', 'f', 'j', 'h', 'd', 'b']
    x, y = func(line1, line2, n)
    print(x, y)
