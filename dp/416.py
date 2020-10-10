# -*- coding: utf-8 -*-
# 2020-10-11 04:24:41
# !@author: superMC @email: 18758266469@163.com
# !@title: partition-equal-subset-sum.py

# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  注意: 
# 
#  
#  每个数组中的元素不会超过 100 
#  数组的大小不会超过 200 
#  
# 
#  示例 1: 
# 
#  输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#  
# 
#  
# 
#  示例 2: 
# 
#  输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
#  
# 
#  
#  Related Topics 动态规划 
#  👍 439 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartition(self, nums):
        sums = sum(nums)
        if sums % 2 == 1:
            return False
        target = sums // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [3, 3, 3, 4, 5]
    ret = Solution().canPartition(nums)
    print(ret)
