# -*- coding: utf-8 -*-
# 2020-11-16 09:51:56
# !@author: superMC @email: 18758266469@163.com
# !@title: maximum-subarray.py

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2628 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [0] * nums_len
        for i in range(nums_len):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans = Solution().maxSubArray(nums)
print(ans)
