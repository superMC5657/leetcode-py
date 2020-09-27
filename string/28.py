# -*- coding: utf-8 -*-
# !@time: 2020-09-24 12:16:57
# !@author: superMC @email: 18758266469@163.com
# !@question title: implement-strstr

# 实现 strStr() 函数。 
# 
#  给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如
# 果不存在，则返回 -1。 
# 
#  示例 1: 
# 
#  输入: haystack = "hello", needle = "ll"
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#  
# 
#  说明: 
# 
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 
# 
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。 
#  Related Topics 双指针 字符串 
#  👍 576 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        n = len(needle)
        m = len(haystack)
        j = 0
        pnext = self.getnext(needle)
        for i in range(m):
            while j > 0 and needle[j] != haystack[i]:
                j = pnext[j]
            if needle[j] == haystack[i]:
                j += 1
                if j == n:
                    return i - n + 1
        return -1

    def getnext(self, s):
        n = len(s)
        pnext = [0, 0]  # 多一个前导0是为了方便后续指针跳跃，避免死循环
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pnext[j]  # 指针跳跃
            if s[j] == s[i]:
                j += 1
            pnext.append(j)
        return pnext


# leetcode submit region end(Prohibit modification and deletion)

