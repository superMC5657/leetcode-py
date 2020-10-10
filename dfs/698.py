# -*- coding: utf-8 -*-
# 2020-10-11 03:25:32
# !@author: superMC @email: 18758266469@163.com
# !@title: partition-to-k-equal-sum-subsets.py

# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。 
# 
#  示例 1： 
# 
#  输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= len(nums) <= 16 
#  0 < nums[i] < 10000 
#  
#  Related Topics 递归 动态规划 
#  👍 253 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        nums_average, remainder = divmod(nums_sum, k)
        if remainder:
            return False
        nums.sort(reverse=True)
        if nums[0] > nums_average:
            return False
        vis = set()

        # 其中total表示当前集合的总和，times表示已经完成的集合数量
        def DFS(total, times):
            if total == nums_average:
                times += 1
                total = 0
            if not total and times == k and len(vis) == len(nums):
                return True
            for i in range(len(nums)):
                # 相同的元素，之前没用上现在肯定也用不上
                if i and nums[i] == nums[i - 1] and i - 1 not in vis:
                    continue
                if i not in vis and total + nums[i] <= nums_average:
                    vis.add(i)
                    if DFS(total + nums[i], times):
                        return True
                    vis.remove(i)
            return False

        return DFS(0, 0)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6]
    k = 3
    ret = Solution().canPartitionKSubsets(nums, k)
    print(ret)
