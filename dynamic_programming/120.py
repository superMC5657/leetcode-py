# -*- coding: utf-8 -*-
# !@time: 2020/6/17 00 44
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 120.py


'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
'''


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[triangle[0][0]]]
        for i in range(1, m):
            dpi = []
            for j in range(len(triangle[i])):
                if j == 0:
                    dpi.append(dp[i - 1][j] + triangle[i][j])
                elif j == len(triangle[i]) - 1:
                    dpi.append(dp[i - 1][j - 1] + triangle[i][j])
                else:
                    dpi.append(min(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j]))

            dp.append(dpi)
        return min(dp[m - 1])

    def minimumTotal_saveMemory(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        cur = triangle[0]
        for i in range(1, m):
            previous = cur
            cur = []
            for j in range(len(triangle[i])):
                if j == 0:
                    cur.append(previous[j] + triangle[i][j])
                elif j == len(triangle[i]) - 1:
                    cur.append(previous[j - 1] + triangle[i][j])
                else:
                    cur.append(min(previous[j - 1] + triangle[i][j], previous[j] + triangle[i][j]))
            del previous
        return min(cur)


if __name__ == '__main__':
    t = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]
    print(Solution().minimumTotal_saveMemory(t))
