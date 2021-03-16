# -*- coding: utf-8 -*-
# !@time: 2021-03-08 13:35:19
# !@author: superMC @email: 18758266469@163.com
# !@question title: palindrome-partitioning-ii

# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。 
# 
#  返回符合要求的 最少分割次数 。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2000 
#  s 仅由小写英文字母组成 
#  
#  
#  
#  Related Topics 动态规划 
#  👍 312 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:
        if s is None and len(s) <= 1:
            return 0
        size = len(s)
        dp = [size - 1] * size
        for i in range(size):
            self.mincutHelper(s, i, i, dp)
            self.mincutHelper(s, i, i + 1, dp)
        return dp[size - 1]

    def mincutHelper(self, s, i, j, dp):
        size = len(s)
        while 0 <= i and j < size and s[i] == s[j]:
            dp[j] = min(dp[j], (-1 if i == 0 else dp[i - 1]) + 1)
            i -= 1
            j += 1

# leetcode submit region end(Prohibit modification and deletion)
