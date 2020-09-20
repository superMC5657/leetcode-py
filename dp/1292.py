# -*- coding: utf-8 -*-
# !@time: 2020/6/9 08 56
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1292.py

"""
给你一个大小为  m x n  的矩阵  mat  和一个整数阈值  threshold。

请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0  。

"""
from typing import List

from tools.utils import prefixAnd


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [0 for i in range(m) for j in range(n)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = mat[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
                if dp[i][j] > threshold:
                    break

    def maxSideLengthv1(self, mat: List[List[int]], threshold: int) -> int:
        if not mat or not mat[0]:
            return 0
        row = len(mat)
        col = len(mat[0])
        # 把前i行j列组成的矩形的面积求出来
        prefix = prefixAnd(row, col, mat)
        left = 0
        right = min(row, col)

        def check(mid):
            for i in range(row - mid + 1):
                for j in range(col - mid + 1):
                    s = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j]
                    if threshold >= s:
                        return True
            return False

        while left <= right:
            # print(left, right)
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right


if __name__ == '__main__':
    mat = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
    t = 4
    Solution().maxSideLengthv1(mat, t)
