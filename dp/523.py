# -*- coding: utf-8 -*-
# !@time: 2020/6/16 23 43
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 523.py

'''给定一个包含 非负数 的数组和一个目标 整数  k，
编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，
且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
'''
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length <= 1:
            return False
        for i in range(length - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True
        if not k:
            return False
        dp = [[nums[0]]]
        for i in range(1, length):
            dpi = []
            for j in dp[i - 1]:
                if (j + nums[i]) % k == 0:
                    return True
                dpi.append(j + nums[i])
            dpi.append(nums[i])
            dp.append(dpi)
        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    print(Solution().checkSubarraySum(nums, k))
