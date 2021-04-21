# -*- coding: utf-8 -*-
# !@time: 2021-04-13 14:31:35	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: longest-palindromic-subsequence.py

# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。 
# 
#  
# 
#  示例 1: 
# 输入: 
# 
#  "bbbab"
#  
# 
#  输出: 
# 
#  4
#  
# 
#  一个可能的最长回文子序列为 "bbbb"。 
# 
#  示例 2: 
# 输入: 
# 
#  "cbbd"
#  
# 
#  输出: 
# 
#  2
#  
# 
#  一个可能的最长回文子序列为 "bb"。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 只包含小写英文字母 
#  
#  Related Topics 动态规划 
#  👍 423 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]
# leetcode submit region end(Prohibit modification and deletion)
