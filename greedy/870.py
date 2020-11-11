# -*- coding: utf-8 -*-
# 2020-09-14 07:38:00
# !@author: superMC @email: 18758266469@163.com
# !@title: advantage-shuffle.py

# 给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。 
# 
#  返回 A 的任意排列，使其相对于 B 的优势最大化。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [2,7,11,15], B = [1,10,4,11]
# 输出：[2,11,7,15]
#  
# 
#  示例 2： 
# 
#  输入：A = [12,24,8,32], B = [13,25,32,11]
# 输出：[24,32,8,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length = B.length <= 10000 
#  0 <= A[i] <= 10^9 
#  0 <= B[i] <= 10^9 
#  
#  Related Topics 贪心算法 数组 
#  👍 77 👎 0

from typing import List

import numpy as np
from scipy.optimize import linear_sum_assignment as linear_assignment


def compute(A, B):
    len_A = len(A)
    len_B = len(B)
    cost_matrix = np.zeros((len_A, len_B), dtype=np.int)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a > b:
                cost_matrix[i, j] = 0
            else:
                cost_matrix[i, j] = 1
    return cost_matrix


class Solution_self:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        len_A = len(A)
        optimal_A = [0] * len_A
        cost_matrix = compute(A, B)
        order = linear_assignment(cost_matrix)[1]
        for i, match in enumerate(order):
            optimal_A[match] = A[i]
        return optimal_A


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    A = [12, 24, 8, 32]
    B = [13, 25, 32, 11]
    ret = Solution().advantageCount(A, B)
    print(ret)
