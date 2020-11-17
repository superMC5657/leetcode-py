# -*- coding: utf-8 -*-
# 2020-11-16 09:37:53
# !@author: superMC @email: 18758266469@163.com
# !@title: maximum-product-subarray.py

# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划 
#  👍 834 👎 0
import sys
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums):
        a, b, res = 1, 1, -sys.maxsize
        for num in nums:
            a, b = max(a * num, b * num, num), min(a * num, b * num, num)
            res = max(res, a)
        return res

# leetcode submit region end(Prohibit modification and deletion)
