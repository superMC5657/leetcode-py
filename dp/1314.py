# -*- coding: utf-8 -*-
# !@time: 2020/6/8
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1314.py
import numpy as np
from scipy import signal

from tools.utils import prefixAnd

'''
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，
其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 
i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。
'''


class Solution:
    def matrixBlockSum(self, mat: list, K: int) -> list:

        np_mat = np.array(mat)
        np_filter = np.ones((2 * K + 1, 2 * K + 1))
        res = signal.convolve2d(np_mat, np_filter, mode='same')
        return res.astype(int).tolist()

    def matrixBlockSum_DP(self, mat: list, K: int) -> list:
        m, n = len(mat), len(mat[0])
        P = prefixAnd(m, n, mat)

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return P[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + get(i - K,
                                                                                                            j - K)
        return ans

    def self_conv(self, mat, k):

        row = len(mat)
        col = len(mat[0])
        n_mat = self.padding(mat, k)
        ans = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                for s in range(i, 2 * k + i + 1):
                    tmp = n_mat[s][j:j + 2 * k + 1]
                    tmp = sum(tmp)
                    ans[i][j] += tmp
        return ans

    def padding(self, mat, k):
        n_mat = []

        row = len(mat)
        col = len(mat[0])
        for i in range(k):
            n_mat.append([0] * (2 * k + col))
        for i in range(row):
            new_line = [0] * k
            new_line.extend(mat[i])
            new_line.extend([0] * k)
            n_mat.append(new_line)
        for i in range(k):
            n_mat.append([0] * (2 * k + col))
        return n_mat


if __name__ == '__main__':
    mat = [[67, 64, 78], [99, 98, 38], [82, 46, 46], [6, 52, 55], [55, 99, 45]]
    k = 1
    solution = Solution()
    n_mat = solution.matrixBlockSum_DP(mat, k)
    print(n_mat)
