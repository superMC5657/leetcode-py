# -*- coding: utf-8 -*-
# !@time: 2020/8/30 2:15 上午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 647.py


"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j] 代表 子串[i, j] 是否是一个 回文串
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        # j = -1
        # while (j := j + 1) < n:
        ''':= 表达式'''
        # 枚举所有可能 因为代表子串 所以 i <= j
        for j in range(n):
            for i in range(0, j + 1):
                # 子串长度
                length = j - i + 1
                # 只有一个字符 直接就是一个回文串
                if length == 1:
                    dp[i][j] = True
                    count += 1
                # 两个字符 只有相等才是回文串
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                # 超过两个字符 首位相同 且除去首尾的子串是回文串 才是回文串
                if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    count += 1
        return count


if __name__ == '__main__':
    m = Solution().countSubstrings("aaa")

    print(m)
