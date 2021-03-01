# -*- coding: utf-8 -*-
# !@time: 2021-02-22 20:19:23	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: combination-sum.py

# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的数字可以无限制重复被选取。 
# 
#  说明： 
# 
#  
#  所有数字（包括 target）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1： 
# 
#  输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
#  
# 
#  示例 2： 
# 
#  输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= candidates.length <= 30 
#  1 <= candidates[i] <= 200 
#  candidate 中的每个元素都是独一无二的。 
#  1 <= target <= 500 
#  
#  Related Topics 数组 回溯算法 
#  👍 1166 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = list()

        def dfs(path, begin, target):

            if target == 0:
                ret.append(path)
                return
            else:
                for index in range(begin, len(candidates)):
                    if target - candidates[index] < 0:
                        break
                    dfs(path + [candidates[index]], index, target - candidates[index])

        if len(candidates) == 0:
            return []
        path = []
        candidates.sort()
        dfs(path, 0, target)
        return ret


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    candidates = [2, 7, 6, 3, 5, 1]
    target = 9
    ret = Solution().combinationSum(candidates, target)
    print(ret)
