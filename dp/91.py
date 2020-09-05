# -*- coding: utf-8 -*-
# !@time: 2020-08-31 17:56:23
# !@author: superMC @email: 18758266469@163.com
# !@question title: decode-ways

# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  示例 1: 
# 
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2: 
# 
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
#  Related Topics 字符串 动态规划 
#  👍 488 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings_self(self, s: str) -> int:
        if s[0] == '0':
            return 0
        s_len = len(s)
        dp = [[] for i in range(s_len)]
        dp[0].append(int(s[0]))
        for i in range(1, s_len):
            num = int(s[i])
            for m in dp[i - 1]:
                if isinstance(m, int):
                    m = [m]
                if num == 0:
                    pass
                else:
                    dp[i].append(m + [num])
                first, second = divmod(m[-1], 10)
                if first == 0 and 0 < second and second * 10 + num <= 26:
                    dp[i].append(m[:-1] + [(second * 10 + num)])
        return len(dp[s_len - 1])

    def numDecodings(self, s: str) -> int:
        size = len(s)
        if s[0] == '0':
            return 0
        # 特判
        if size == 0:
            return 0
        dp = [0] * size
        dp[0] = 1
        for i in range(1, size):
            t = int(s[i])
            if 1 <= t <= 9:
                dp[i] += dp[i - 1]  # 最后一个数字解密成一个字母
            if i >= 1:  # 下面这种情况至少要有两个字符
                t = int(s[i - 1:i + 1])
                if 10 <= t <= 26:
                    if i == 1:
                        dp[i] += 1
                    else:
                        dp[i] += dp[i - 2]  # 最后两个数字解密成一个一个字母
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = 4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948
    print(Solution().numDecodings(s=str(s)))
