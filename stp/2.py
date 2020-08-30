# -*- coding: utf-8 -*-
# !@time: 2020/8/21 8:02 下午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 2.py
import numpy as np


def get_num(n) -> list:
    #  求前n项斐波那契数列
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp


def printMatrix(n):
    dp = get_num(n * n)[::-1]
    matrix = np.zeros((n, n), dtype=int)
    x0 = y0 = 0
    xn = n - 1
    yn = n - 1
    index = 0
    while x0 <= xn and y0 <= yn:
        for y in range(y0, yn + 1):
            matrix[x0][y] = dp[index]
            index += 1
        for x in range(x0 + 1, xn + 1):
            matrix[x][yn] = dp[index]
            index += 1
        if x0 < xn:
            for y in range(yn - 1, y0 - 1, -1):
                matrix[xn][y] = dp[index]
                index += 1
        if y0 < yn:
            for x in range(xn - 1, x0, -1):
                matrix[x][y0] = dp[index]
                index += 1
        x0 += 1
        y0 += 1
        xn -= 1
        yn -= 1
    return matrix


if __name__ == '__main__':
    print(printMatrix(5))
