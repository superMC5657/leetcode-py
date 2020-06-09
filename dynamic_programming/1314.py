# -*- coding: utf-8 -*-
# !@time: 2020/6/8
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1314.py
import numpy as np
from scipy import signal


class Solution:
    def matrixBlockSum(self, mat: list, K: int) -> list:

        np_mat = np.array(mat)
        np_filter = np.ones((2 * K + 1, 2 * K + 1))
        res = signal.convolve2d(np_mat, np_filter, mode='same')
        return res.astype(int).tolist()

    def matrixBlockSum2(self, mat: list, K: int) -> list:

        m = len(mat)
        n = len(mat[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j - K < 0:
                    tmp = 0
                else:
                    tmp = j - K
                ans[i][j] = sum(mat[i][tmp:j + K + 1])
        # print(ans)
        ans2 = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i - K < 0:
                    tmp = 0
                else:
                    tmp = i - K
                if i + K + 1 >= m:
                    tmp2 = m
                else:
                    tmp2 = i + K + 1
                ans2[i][j] = sum([ans[_][j] for _ in range(tmp, tmp2)])
        # print(ans2)
        return ans2

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
    n_mat = solution.self_conv(mat, k)
    print(n_mat)
