# -*- coding: utf-8 -*-
# !@time: 2020-09-15 18:07:40
# !@author: superMC @email: 18758266469@163.com
# !@question title: minimum-window-substring

# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。 
# 
#  
# 
#  示例： 
# 
#  输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC" 
# 
#  
# 
#  提示： 
# 
#  
#  如果 S 中不存这样的子串，则返回空字符串 ""。 
#  如果 S 中存在这样的子串，我们保证它是唯一的答案。 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 745 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        cnt = collections.Counter(t)
        ans = ''
        n = 0  # 当前我满足了 t 中的字母的种数
        l = 0
        for r, ch in enumerate(s):
            if ch not in cnt:
                continue
            cnt[ch] -= 1
            if cnt[ch] == 0:
                n += 1
            while s[l] not in cnt or cnt[s[l]] < 0:  # 看看当前 l 处的字母是否必要，没必要 l 就加1
                if s[l] in cnt:
                    cnt[s[l]] += 1
                l += 1
            if n == len(cnt):
                if not ans or len(ans) > r - l + 1:
                    ans = s[l: r + 1]
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    ret = Solution().minWindow(S, T)
    print(ret)
