# -*- coding: utf-8 -*-
# !@time: 2020-11-01 20:43:14
# !@author: superMC @email: 18758266469@163.com
# !@question title: length-of-last-word

# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。 
# 
#  如果不存在最后一个单词，请返回 0 。 
# 
#  说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。 
# 
#  
# 
#  示例: 
# 
#  输入: "Hello World"
# 输出: 5
#  
#  Related Topics 字符串 
#  👍 251 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_s = s.strip().split(' ')
        if len(list_s) <= 0:
            return 0
        return len(list_s[-1])


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = 'a '
    ret = Solution().lengthOfLastWord(s)
    print(ret)
