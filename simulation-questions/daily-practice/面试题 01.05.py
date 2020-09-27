# -*- coding: utf-8 -*-
# 2020-09-18 10:03:34
# !@author: superMC @email: 18758266469@163.com
# !@title: one-away-lcci.py

# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 
# first = "pale"
# second = "ple"
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  输入: 
# first = "pales"
# second = "pal"
# 输出: False
#  
#  Related Topics 字符串 动态规划 
#  👍 36 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def EditAway(self, first: str, second: str) -> bool:
        less_one = self.__minDistance(first, second) <= 1
        return less_one

    def __minDistance(cls, word1: str, word2: str) -> int:
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

    def oneEditAway(self, first: str, second: str) -> bool:
        # 编辑距离为1时：
        # 插入字符串或者删除字符串意味着两个字符串长度相差1
        # 替换字符意味着长度相等
        # 编辑距离为0时：两字符串相等
        if first == second:
            return True
        if abs(len(first) - len(second)) > 1:
            return False

        i, j, count = 0, 0, 0  # 设置指针和相异数统计变量
        if len(first) == len(second):
            while i < len(first):
                if first[i] != second[j]:
                    count += 1
                    if count > 1:
                        return False
                i += 1
                j += 1
        else:
            if len(first) < len(second):
                first, second = second, first
            while i < len(first) and j < len(second):
                if first[i] != second[j]:
                    count += 1
                    if count > 1:
                        return False
                    i += 1
                else:
                    i += 1
                    j += 1
            if i < len(first):  # 较长字符串的指针若没有完整的遍历一次，count+1
                count += 1

        return count <= 1

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    first = "pale"
    second = "ple"
    ret = Solution().oneEditAway(first, second)
    print(ret)
