# -*- coding: utf-8 -*-
# 2020-09-09 20:01:04
# !@author: superMC @email: 18758266469@163.com
# !@title: integer-break.py

# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。 
# 
#  示例 2: 
# 
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
#  说明: 你可以假设 n 不小于 2 且不大于 58。 
#  Related Topics 数学 动态规划 
#  👍 368 👎 0
from functools import lru_cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @lru_cache
    def integerBreak_rec(self, n: int) -> int:
        if n == 2:
            return 1
        res = 0
        for i in range(1, n):
            res = max(res, max(i * self.integerBreak(n - i), i * (n - i)))
        return res

    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])
                # 有些情况(i-j) * j更大 当i比较小的时候
        return dp[n]

    def integerBreak_math(self, n: int) -> int:
        if n == 2:
            return 1

        if n == 3:
            return 2

        a = 1
        while n > 4:
            n = n - 3
            a = a * 3

        return a * n


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # ret_rec = Solution().integerBreak_rec(1158)
    # ret_dp = Solution().integerBreak(11508)
    ret_math = Solution().integerBreak_math(11508)
    import math

    print(math.log10(ret_math))
