# -*- coding: utf-8 -*-
# !@time: 2021-03-04 15:11:41	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: permutations-ii.py

# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics 回溯算法 
#  👍 612 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(pre, others):
            if not others:
                res.append(pre)
                return
            for i, new_ele in enumerate(others):
                if others[i] == others[i + 1]:
                    return
                left = pre[:]
                left.append(new_ele)
                right = others[:]
                right.remove(new_ele)
                dfs(left, right)

        dfs([], nums)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1, 1, 2]
    res = Solution().permuteUnique(nums)
    print(res)
