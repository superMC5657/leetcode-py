# -*- coding: utf-8 -*-
# !@time: 2020-06-05 05:11
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1.py
from memory_profiler import profile
from sys import stdin
from tools.generate_n_m_dim_array import random_n_md


@profile
def solve(data):
    # data.sort(key=lambda k: k[1], reverse=True)
    data = sorted(data, key=lambda k: k[1], reverse=True)
    res = [data[0]]
    for i in range(1, len(data)):
        if data[i][0] > res[-1][0]:
            res.append(data[i])
        else:
            continue
    res.sort(key=lambda k: k[0])
    for i in res:
        print(i[0], i[1])


def main():
    n = int(stdin.readline().strip())
    point = []
    for i in range(n):
        point.append([int(x) for x in stdin.readline().strip().split()])
    solve(point)


if __name__ == '__main__':
    n = 500000
    point = random_n_md(n, 2)
    solve(point)
