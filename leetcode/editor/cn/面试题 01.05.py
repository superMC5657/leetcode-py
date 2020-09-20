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
    def oneEditAway(self, first: str, second: str) -> bool:
# leetcode submit region end(Prohibit modification and deletion)
