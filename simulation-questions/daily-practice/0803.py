# -*- coding: utf-8 -*-
# !@time: 2020/7/31 06 48
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 0803.py

"""
https://leetcode-cn.com/problems/magic-index-lcci/
面试题 08.03. 魔术索引
魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

示例1:

 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0
示例2:

 输入：nums = [1, 1, 1]
 输出：1
提示:

nums长度在[1, 1000000]之间
"""
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        # 做两次二分查找
        res1 = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == nums[mid]:
                res1 = mid
                r = mid - 1
            elif mid < nums[mid]:  # 第一类情况
                r = mid - 1
            else:
                l = mid + 1

        res2 = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == nums[mid]:
                res2 = mid
                r = mid - 1
            elif mid > nums[mid]:  # 第二类情况
                r = mid - 1
            else:
                l = mid + 1

        if res1 == res2:
            return res1
        if res1 == -1:
            return res2
        if res2 == -1:
            return res1
        return min(res1, res2)


if __name__ == '__main__':
    Solution().findMagicIndex()
