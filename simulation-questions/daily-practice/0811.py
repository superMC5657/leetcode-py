# -*- coding: utf-8 -*-
# !@time: 2020/6/17 14 01
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 0811.py
"""硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)"""


class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25, 10, 5, 1]
        # 注意dp的初始化，表示没有硬币情况下凑金额0-n分
        dp = [0] * (n + 1)
        dp[0] = 1  # 没有硬币凑0分为1种方式
        for i in range(len(coins)):
            for j in range(coins[i], n + 1):
                dp[j] += dp[j - coins[i]]
        return dp[-1] % 1000000007

    def waysToChange_dp(self, n: int) -> int:
        coins = [25, 10, 5, 1]
        # 注意dp的初始化，表示没有硬币情况下凑金额0-n分
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(n + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for j in range(n + 1):
            dp[0][j] = 0
        for i in range(len(coins) + 1):
            for j in range(coins[i], n + 1):
                dp[j] += dp[j - coins[i]]
        return dp[-1] % 1000000007

    def waysToChange_math(self, n: int) -> int:
        n = n // 5
        ans = 0
        while n >= 0:
            ans = (ans + (n // 2 + 1) * ((n + 1) // 2 + 1))
            n -= 5
        return ans % 1000000007


if __name__ == '__main__':
    print(Solution().waysToChange_math(10000))
