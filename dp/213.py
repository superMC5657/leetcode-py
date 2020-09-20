# -*- coding: utf-8 -*-
# 2020-09-09 03:54:07
# !@author: superMC @email: 18758266469@163.com
# !@title: house-robber-ii.py

# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋
# 装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。 
# 
#  示例 1: 
# 
#  输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#  
# 
#  示例 2: 
# 
#  输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#       偷窃到的最高金额 = 1 + 3 = 4 。
#  Related Topics 动态规划 
#  👍 364 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_len = len(nums)
        if nums_len <= 3:
            return max(nums)

        dp = [[0] * 2 for _ in range(nums_len)]  # 最大偷窃到的金额
        dp[0][0] = 0
        dp[0][1] = nums[0]
        dp[1][0] = nums[1]
        dp[1][1] = nums[0]
        for i in range(2, nums_len - 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][0] + nums[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][1] + nums[i])
        dp[-1][0] = max(dp[- 2][0], dp[- 3][0] + nums[-1])
        dp[-1][1] = dp[-2][1]
        return max(dp[-1][0], dp[-1][1])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    ret = Solution().rob([1, 7, 9, 2])
    print(ret)
