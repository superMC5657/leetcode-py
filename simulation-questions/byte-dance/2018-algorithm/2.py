# -*- coding: utf-8 -*-
# !@time: 2020-06-06 01:14
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 2.py

from sys import stdin


def main():
    n = int(stdin.readline().strip())
    data = [int(x) for x in stdin.readline().strip().split()]
    print(solve2(data))


def solve(data):
    # data.sort(reverse=True)
    n = len(data)
    res = 0
    for i in range(n):
        n_sum = 0
        min_num = data[i]
        for j in range(i, n):
            n_sum += data[j]
            min_num = min(min_num, data[j])
            res = max(res, min_num * n_sum)

    return res


# 以每个数为最小值找到左右边界
def solve2(data):
    stack = []
    stack_pop_before = []
    ans = 0
    for index, curNum in enumerate(data):
        pop_sum = 0
        pop_before = 0
        while stack and curNum < stack[-1]:
            pop_num = stack.pop()
            pop_sum += pop_num
            pop_before += stack_pop_before.pop()
            ans = max(ans, (pop_before + pop_sum) * pop_num)
        stack_pop_before.append(pop_before + pop_sum)
        stack.append(curNum)
    return ans


if __name__ == '__main__':
    main()
