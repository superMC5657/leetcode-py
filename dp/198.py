# -*- coding: utf-8 -*-
# !@time: 2020-08-31 20:46:28
# !@author: superMC @email: 18758266469@163.com
# !@question title: house-robber

# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上
# 被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 
#  示例 2： 
# 
#  输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics 动态规划 
#  👍 1046 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]

        dp = [0] * nums_len  # 最大偷窃到的金额
        dp[0] = nums[0]
        dp[1] = nums[1] if nums[1] > nums[0] else nums[0]
        if nums_len == 2:
            return dp[1]
        for i in range(2, nums_len):
            this_choose = dp[i - 2] + nums[i]
            if this_choose > dp[i - 1]:
                dp[i] = this_choose
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    ret = Solution().rob([2, 7, 9, 3, 1])
    print(ret)
