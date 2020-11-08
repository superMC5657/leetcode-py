# -*- coding: utf-8 -*-
# !@time: 2020-10-21 20:31:27
# !@author: superMC @email: 18758266469@163.com
# !@question title: palindromic-substrings

# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  输入的字符串长度不会超过 1000 。 
#  
#  Related Topics 字符串 动态规划 
#  👍 423 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings_n2(self, s: str) -> int:
        n = len(s)
        self.res = 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                self.res += 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res

    def countSubstrings(self, s: str) -> int:
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        pos, max_right = 0, 0
        rl = [0 for _ in range(n)]
        for i in range(n):
            if i < max_right:
                rl[i] = min(rl[2 * pos - i], max_right - i)
            else:
                rl[i] = 1
            while i - rl[i] >= 0 and i + rl[i] < n and s[i - rl[i]] == s[i + rl[i]]:
                rl[i] += 1
            if rl[i] + i - 1 > max_right:
                max_right = rl[i] + i - 1
                pos = i
        return sum(x // 2 for x in rl)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ret = Solution().countSubstrings("abc")
    print(ret)
