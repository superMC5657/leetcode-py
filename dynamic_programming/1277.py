# -*- coding: utf-8 -*-
# !@time: 2020/6/9 08 11
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1277.py
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return sum(matrix)
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans += dp[i][j]
        return ans
