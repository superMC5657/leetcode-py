# -*- coding: utf-8 -*-
# 2020-09-04 14:26:35
# !@author: superMC @email: 18758266469@163.com
# !@title: best-time-to-buy-and-sell-stock.py

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
# 
#  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。 
# 
#  注意：你不能在买入股票前卖出股票。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#  
# 
#  示例 2: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
#  Related Topics 数组 动态规划 
#  👍 1174 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_len = len(prices)
        if p_len <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(0, p_len):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    ret = Solution().maxProfit(prices=[7, 6, 5, 4, 2, 6])
    print(ret)
