# -*- coding: utf-8 -*-
# !@time: 2021-04-01 09:48:03
# !@author: superMC @email: 18758266469@163.com
# !@question title: clumsy-factorial

# 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 *
#  3 * 2 * 1。 
# 
#  相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)
# 和减法(-)。 
# 
#  例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我
# 们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。 
# 
#  另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。 
# 
#  实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。 
# 
#  
# 
#  示例 1： 
# 
#  输入：4
# 输出：7
# 解释：7 = 4 * 3 / 2 + 1
#  
# 
#  示例 2： 
# 
#  输入：10
# 输出：12
# 解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10000 
#  -2^31 <= answer <= 2^31 - 1 （答案保证符合 32 位整数。） 
#  
#  Related Topics 数学 
#  👍 44 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def clumsy(self, N: int) -> int:
        # 处理4个一组的数字
        def pending_nums(a, b, c, d):
            return -int(a * b / c) + d

        # 阶乘
        def multi_num(num):
            # 如果为0，这里返回0
            if num == 0:
                return 0
            if num == 1:
                return 1
            return num * multi_num(num - 1)

        # 小于4的N，直接返回N的阶乘
        if N < 4:
            return multi_num(N)
        k = N // 4
        result = 0
        # 首先加上开头的2 * (int(N * (N - 1) / (N - 2))) ，目的为了4个一组方便处理
        result += 2 * (int(N * (N - 1) / (N - 2)))
        while k:
            # 处理4个一组的数据
            result = result + pending_nums(N, N - 1, N - 2, N - 3)
            N -= 4
            k -= 1
        # 不够4个一组的进行处理
        if N < 4:
            return result - multi_num(N)

# leetcode submit region end(Prohibit modification and deletion)
