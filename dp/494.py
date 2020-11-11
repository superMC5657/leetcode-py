# -*- coding: utf-8 -*-
# !@time: 2020-11-08 15:23:43
# !@author: superMC @email: 18758266469@163.com
# !@question title: target-sum

# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选
# 择一个符号添加在前面。 
# 
#  返回可以使最终数组和为目标数 S 的所有添加符号的方法数。 
# 
#  
# 
#  示例： 
# 
#  输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# 一共有5种方法让最终目标和为3。
#  
# 
#  
# 
#  提示： 
# 
#  
#  数组非空，且长度不会超过 20 。 
#  初始的数组的和不会超过 1000 。 
#  保证返回的最终结果能被 32 位整数存下。 
#  
#  Related Topics 深度优先搜索 动态规划 
#  👍 459 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays_mine(self, nums: List[int], S: int) -> int:
        nums_len = len(nums)
        dp = [{} for _ in range(nums_len)]
        if nums[-1] != 0:
            dp[nums_len - 1] = {S - nums[-1]: 1, S + nums[-1]: 1}
        else:
            dp[nums_len - 1] = {S: 2}

        for i in range(nums_len - 2, -1, -1):
            for key, value in dp[i + 1].items():
                if key - nums[i] not in dp[i].keys():
                    dp[i][key - nums[i]] = value
                else:
                    dp[i][key - nums[i]] += value
                if key + nums[i] not in dp[i].keys():
                    dp[i][key + nums[i]] = value
                else:
                    dp[i][key + nums[i]] += value

        if 0 in dp[0].keys():
            return dp[0][0]
        else:
            return 0

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        p = (sum(nums) + S) // 2  # 正子集合的目标和
        dp = [1] + [0] * p
        for num in nums:
            for j in range(p, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[p]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1]
    S = 2
    ret = Solution().findTargetSumWays(nums, S)
    print(ret)
