# -*- coding: utf-8 -*-
# !@time: 2021-03-01 17:15:13
# !@author: superMC @email: 18758266469@163.com
# !@question title: permutations

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 1161 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(pre, others):
            if not others:
                res.append(pre)
                return
            for new_ele in others:
                left = pre[:]
                left.append(new_ele)
                right = others[:]
                right.remove(new_ele)
                dfs(left, right)

        dfs([], nums)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1, 2, 3]
    ret = Solution().permute(nums)
    print(ret)
