# -*- coding: utf-8 -*-
# !@time: 2020/7/24 22 52
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 63.py

"""
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([5, 1, 3, 4, 34, 1, 5, 4]))
