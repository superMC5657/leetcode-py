# -*- coding: utf-8 -*-
# !@time: 2020-06-16 07:18
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 96.py

'''给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？'''


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        # 考虑有第零个 即为空子数情况
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[i - j] * dp[j - 1]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numTrees(19))
