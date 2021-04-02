# -*- coding: utf-8 -*-
# !@time: 2021-04-03 01:12:38
# !@author: superMC @email: 18758266469@163.com
# !@question title: longest-common-subsequence

# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。 
# 
#  一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。 
# 
#  
#  例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。 
#  
# 
#  两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：text1 = "abcde", text2 = "ace" 
# 输出：3  
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
#  
# 
#  示例 3： 
# 
#  
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text1.length, text2.length <= 1000 
#  text1 和 text2 仅由小写英文字符组成。 
#  
#  Related Topics 动态规划 
#  👍 417 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 is None or text2 is None:
            return 0
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # 说明只有当前位置匹配上了
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    text1 = "abcde"
    text2 = "cdefg"
    ret = Solution().longestCommonSubsequence(text1, text2)
    print(ret)
