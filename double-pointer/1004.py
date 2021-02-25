# -*- coding: utf-8 -*-
# !@time: 2021-02-19 14:55:19	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: max-consecutive-ones-iii.py

# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。 
# 
#  返回仅包含 1 的最长（连续）子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释： 
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。 
# 
#  示例 2： 
# 
#  输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20000 
#  0 <= K <= A.length 
#  A[i] 为 0 或 1 
#  
#  Related Topics 双指针 Sliding Window 
#  👍 199 👎 0


from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from queue import Queue


# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#         left = right = 0
#         q_zeros = Queue(maxsize=K + 1)
#         maxsize = 0
#         for index, element in enumerate(A):
#             if element == 0:
#                 q_zeros.put(index)
#                 if q_zeros.qsize() == K + 1:
#                     left = q_zeros.get() + 1
#             maxsize = max(maxsize, index - left + 1)
#         return max(maxsize, K)


class Solution(object):
    def longestOnes(self, A, K):
        N = len(A)
        res = 0
        left, right = 0, 0
        zeros = 0
        while right < N:
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    ret = Solution().longestOnes(A, K)
    print(ret)
