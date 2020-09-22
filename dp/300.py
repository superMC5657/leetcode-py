# -*- coding: utf-8 -*-
# !@time: 2020-09-08 20:25:11
# !@author: superMC @email: 18758266469@163.com
# !@question title: longest-increasing-subsequence

# 给定一个无序的整数数组，找到其中最长上升子序列的长度。 
# 
#  示例: 
# 
#  输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
#  说明: 
# 
#  
#  可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
#  你算法的时间复杂度应该为 O(n2) 。 
#  
# 
#  进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 
#  Related Topics 二分查找 动态规划 
#  👍 960 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ret = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(ret)
