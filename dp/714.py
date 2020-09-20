# -*- coding: utf-8 -*-
# !@time: 2020-06-16 08:56
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 714.py

'''给定一个整数数组  prices，其中第  i  个元素代表了第  i  天的股票价格 ；非负整数  fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        # 构造状态转移方程
        states = 2
        dp = [[0] * states for _ in range(days)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, days):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return dp[days - 1][0]


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution.maxProfit(super, prices, fee))
