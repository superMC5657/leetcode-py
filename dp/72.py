# -*- coding: utf-8 -*-
# 2020-09-05 05:07:28
# !@author: superMC @email: 18758266469@163.com
# !@title: edit-distance.py

# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
#  Related Topics 字符串 动态规划 
#  👍 1118 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 自顶向下的递归
    def minDistance_rec(self, word1: str, word2: str) -> int:
        # 出口
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        # 相等 则求子串
        if word1[-1] == word2[-1]:
            return self.minDistance_rec(word1[:-1], word2[:-1])
        else:
            return 1 + min(self.minDistance_rec(word1[:-1], word2[:-1]), self.minDistance_rec(word1[:-1], word2),
                           self.minDistance_rec(word1, word2[:-1]))
            # self.minDistance(word1 + word2[-1], word2)

    # 自低向上的dp
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # 有一个字符串为空串
        if m == 0 or n == 0:
            return m + n

        # DP 数组
        # 考虑到空的情况
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 边界状态初始化
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    word1 = "intention"
    word2 = "execution"
    ret = Solution().minDistance(word1, word2)
    print(ret)
