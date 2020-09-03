# -*- coding: utf-8 -*-
# !@time: 2020-06-20 20:47
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1477.py
from typing import List

"""
给你一个整数数组 arr 和一个整数值 target 。
请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。
可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。
请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。
"""


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        res = n + 1

        pre = {}
        pre[0] = -1
        dp = [float('inf')] * n

        p = 0
        for i, a in enumerate(arr):
            p += a
            dp[i] = dp[i - 1]
            if (p - target) in pre:
                cur = i - pre[p - target]
                if pre[p - target] >= 0 and dp[pre[p - target]] != float('inf'):
                    res = min(res, cur + dp[pre[p - target]])
                dp[i] = min(i - pre[p - target], dp[i - 1])
            pre[p] = i
        print(pre)
        return -1 if res == n + 1 else res


if __name__ == '__main__':
    arr = [3, 2, 2, 4, 3]
    target = 3
    Solution().minSumOfLengths(arr, target)
