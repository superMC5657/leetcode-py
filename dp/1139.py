# -*- coding: utf-8 -*-
# !@time: 2020/7/24 22 53
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1139.py

"""
1139. 最大的以 1 为边界的正方形
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，
并返回该子网格中的元素数量。如果不存在，则返回 0。
https://leetcode-cn.com/problems/coin-lcci/
"""
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid) -> int:

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        maxLen = 0
        m, n = len(grid), len(grid[0])
        # 遍历每个点
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag1 = True
                    currLen = maxLen
                    while i + currLen < m and j + currLen < n:
                        flag2 = True
                        # 如果‘左边界‘有0， 那么检查下一个点
                        for a in range(i, i + currLen + 1):
                            if grid[a][j] != 1:
                                flag1 = False
                                break
                        if not flag1:
                            break
                        # 如果‘上边界‘有0， 那么检查下一个点
                        for b in range(j, j + currLen + 1):
                            if grid[i][b] != 1:
                                flag1 = False
                                break
                        if not flag1:
                            break
                        # 如果’右边界’有0， 那么继续在这一点，检查边长+1的正方形
                        for a in range(i, i + currLen + 1):
                            if grid[a][j + currLen] != 1:
                                currLen += 1
                                flag2 = False
                                break
                        if not flag2:
                            continue
                        # 如果’下边界’有0， 那么继续在这一点，检查边长+1的正方形
                        for b in range(j, j + currLen + 1):
                            if grid[i + currLen][b] != 1:
                                currLen += 1
                                flag2 = False
                                break
                        if not flag2:
                            continue
                        currLen += 1
                        maxLen = currLen
        return maxLen * maxLen


if __name__ == '__main__':
    print(Solution().largest1BorderedSquare())
