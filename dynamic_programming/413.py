# -*- coding: utf-8 -*-
# !@time: ${DATE} ${TIME}
# !@author: superMC @email: 18758266469@163.com
# !@fileName: ${NAME}.py

# 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。 
# 
#  例如，以下数列为等差数列: 
# 
#  
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9 
# 
#  以下数列不是等差数列。 
# 
#  
# 1, 1, 2, 5, 7 
# 
#  
# 
#  数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。 
# 
#  如果满足以下条件，则称子数组(P, Q)为等差数组： 
# 
#  元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。 
# 
#  函数要返回数组 A 中所有为等差数组的子数组个数。 
# 
#  
# 
#  示例: 
# 
#  
# A = [1, 2, 3, 4]
# 
# 返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
#  
#  Related Topics 数学 动态规划 
#  👍 164 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        def is_ari_seq(l: List[int]):
            if len(l) < 3:
                return False, None
            dec = l[1] - l[0]
            for i in range(2, len(l)):
                if dec == l[i] - l[i - 1]:
                    continue
                else:
                    return False, None
            return True, dec

        a_len = len(A)
        dp = [0] * a_len

        if a_len < 3:
            return 0
        flag = True
        for i in range(2, a_len):
            if flag:
                dp_i_is_ari, dp_i_dec = is_ari_seq(A[i - 2:i + 1])
                if dp_i_is_ari:
                    dp[i] = 1 + dp[i - 1]
                    flag = False
                    cache = 1
                else:
                    dp[i] = dp[i - 1]
            else:
                if A[i] - A[i - 1] == dp_i_dec:
                    cache += 1
                    dp[i] = dp[i - 1] + cache

                else:
                    flag = True
                    dp[i] = dp[i - 1]
        return dp[a_len - 1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]))
