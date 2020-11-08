# -*- coding: utf-8 -*-
# !@time: 2020-10-21 20:25:14
# !@author: superMC @email: 18758266469@163.com
# !@question title: longest-palindromic-substring

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2823 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        length = len(s)
        if length == 1 or s == s[::-1]: return s
        max_len, start = 1, 0
        for i in range(1, length):
            even = s[i - max_len:i + 1]
            odd = s[i - max_len - 1:i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
        return s[start:start + max_len]
# leetcode submit region end(Prohibit modification and deletion)
