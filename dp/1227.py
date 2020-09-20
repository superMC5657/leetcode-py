# -*- coding: utf-8 -*-
# !@time: 2020/6/17 12 33
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1227.py

"""
有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。

剩下的乘客将会：

如果他们自己的座位还空着，就坐到自己的座位上，

当他们自己的座位被占用时，随机选择其他座位
第 n  位乘客坐在自己的座位上的概率是多少？
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return self.cal_helper(n)

    def cal_helper(self, n):
        if n > 1:
            return 1 / n + (n - 2) / n * self.cal_helper(n - 1)
        else:
            return 1

    def nthPersonGetsNthSeat_dp(self, n: int) -> float:
        dp = [0] * n
        dp[0] = 1.0
        for i in range(1, n):
            dp[i] = 1 / (i + 1) + (i - 1) / (i + 1) * dp[i - 1]
        return dp[n - 1]


if __name__ == '__main__':
    print(Solution().nthPersonGetsNthSeat_dp(2))
