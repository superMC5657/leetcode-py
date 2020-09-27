# -*- coding: utf-8 -*-
# !@time: 2020/9/25 下午2:38
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1.py


def solution(x):
    dp = [0] * x
    dp[0] = 1
    dp[1] = 2
    for i in range(2, x):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


if __name__ == '__main__':
    x = 19
    print(solution(x))
