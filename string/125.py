# -*- coding: utf-8 -*-
# !@time: 2020-11-08 14:49:39
# !@author: superMC @email: 18758266469@163.com
# !@question title: valid-palindrome

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串 
#  👍 288 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
import re


class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.strip().lower())
        if not s:
            return True

        s_size = len(s)
        low = 0
        high = s_size - 1
        while low <= high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ret = Solution().isPalindrome("A man, a plan, a canal: Panama")
    print(ret)
