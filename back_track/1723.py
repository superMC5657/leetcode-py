# -*- coding: utf-8 -*-
# !@time: 2021-05-08 00:45:23
# !@author: superMC @email: 18758266469@163.com
# !@question title: find-minimum-time-to-finish-all-jobs

# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。 
# 
#  请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你
# 设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。 
# 
#  返回分配方案中尽可能 最小 的 最大工作时间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= jobs.length <= 12 
#  1 <= jobs[i] <= 107 
#  
#  Related Topics 递归 回溯算法 
#  👍 60 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def dfs(nums, groups, target):  # groups[i]代表第i个工人所用的时间
            if not nums: return True  # nums为空说明工作都分完了，可以在target时间内由k名工人完成所有工作
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if dfs(nums, groups, target): return True
                    groups[i] -= v
                if not group: break  # 剪枝
            nums.append(v)
            return False

        jobs.sort()
        l, r = jobs[-1], sum(jobs)
        while l < r:
            mid = l + (r - l) // 2
            if dfs(jobs[:], [0] * k, mid):
                r = mid
            else:
                l = mid + 1
        return l
# leetcode submit region end(Prohibit modification and deletion)

