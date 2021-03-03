# -*- coding: utf-8 -*-
# !@time: 2021-03-02 22:42:04	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: combination-sum-ii.py

# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用一次。 
# 
#  说明： 
# 
#  
#  所有数字（包括目标数）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#  
# 
#  示例 2: 
# 
#  输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ] 
#  Related Topics 数组 回溯算法 
#  👍 510 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        ret = []

        def dfs(begin, path, target):

            for i in range(begin + 1, len(candidates)):
                if i > begin + 1 and candidates[i] == candidates[i - 1]:
                    continue
                if target - candidates[i] < 0:
                    break
                elif target - candidates[i] == 0:
                    ret.append(path + [candidates[i]])
                else:
                    dfs(i, path + [candidates[i]], target - candidates[i])

        dfs(-1, [], target)
        return ret


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    candidates = [2, 5, 2, 1, 2]
    target = 5
    res = Solution().combinationSum2(candidates, target)
    print(res)
