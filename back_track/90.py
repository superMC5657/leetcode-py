# -*- coding: utf-8 -*-
# !@time: 2021-03-31 01:34:07	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: subsets-ii.py

# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  
#  
#  Related Topics 数组 回溯算法 
#  👍 429 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        size = len(nums)
        nums.sort()

        def dfs(cur, index):
            index += 1
            ret.append(cur)
            for index_2 in range(index, size):
                if index_2 - index > 0 and nums[index_2] == nums[index_2 - 1]:
                    continue
                dfs(cur + [nums[index_2]], index_2)

        dfs([], -1)
        return ret


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1, 2, 2]
    ret = Solution().subsetsWithDup(nums)
    print(ret)
