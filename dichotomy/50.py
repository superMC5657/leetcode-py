# -*- coding: utf-8 -*-
# !@time: 2021-01-10 09:38:07
# !@author: superMC @email: 18758266469@163.com
# !@question title: powx-n

# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。 
# 
#  示例 1: 
# 
#  输入: 2.00000, 10
# 输出: 1024.00000
#  
# 
#  示例 2: 
# 
#  输入: 2.10000, 3
# 输出: 9.26100
#  
# 
#  示例 3: 
# 
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25 
# 
#  说明: 
# 
#  
#  -100.0 < x < 100.0 
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。 
#  
#  Related Topics 数学 二分查找 
#  👍 567 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPow_(self, x: float, n: int) -> float:
        return pow(x, n)

    def myPow(self, x: float, n: int) -> float:
        def inner_myPow(x, n):
            # 定义终止条件
            if n == 1: return x
            if n == 0: return 1
            # 定义分治后的乘积
            y = inner_myPow(x, n // 2)
            # 偶数时直接y的平方
            if n % 2 == 0:
                return y * y
            # 奇数时需要多乘一个x
            else:
                return y * y * x

        # 当指数小于0时，转出大于0再进行运算
        if n < 0: return 1 / self.myPow(x, -n)
        return inner_myPow(x, n)
# leetcode submit region end(Prohibit modification and deletion)
