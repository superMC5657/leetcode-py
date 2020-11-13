# -*- coding: utf-8 -*-
# !@time: 2020-11-12 18:34:59
# !@author: superMC @email: 18758266469@163.com
# !@question title: minimum-ascii-delete-sum-for-two-strings

# 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。 
# 
#  示例 1: 
# 
#  
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
#  
# 
#  示例 2: 
# 
#  
# 输入: s1 = "delete", s2 = "leet"
# 输出: 403
# 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
# 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
# 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
# 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
#  
# 
#  注意: 
# 
#  
#  0 < s1.length, s2.length <= 1000。 
#  所有字符串中的字符ASCII值在[97, 122]之间。 
#  
#  Related Topics 动态规划 
#  👍 166 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        m = len(s1)
        n = len(s2)

        # DP 数组
        # 考虑到空的情况
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        he = 0
        for i in range(1, m + 1):  # 处理边界
            he += ord(s1[i - 1])
            dp[i][0] = he
        he = 0
        for i in range(1, n + 1):
            he += ord(s2[i - 1])
            dp[0][i] = he

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + ord(s1[i - 1]) + ord(s2[j - 1]), dp[i - 1][j] + ord(s1[i - 1]),
                                   dp[i][j - 1] + ord(s2[j - 1]))
        return dp[m][n]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s1 = "delete"
    s2 = "leet"
    ret = Solution().minimumDeleteSum(s1, s2)
    print(ret)
