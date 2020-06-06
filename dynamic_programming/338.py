# -*- coding: utf-8 -*-
# !@time: 2020-06-07 01:37
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 338.py
import json


class Solution:
    def countBits(self, num: int) -> list:
        oneNums_array = []

        for i in range(num + 1):
            curNum = i
            oneCounts = 0
            while curNum:
                if curNum % 2 == 1:
                    oneCounts += 1
                curNum = curNum // 2
            oneNums_array.append(oneCounts)
        return oneNums_array

    def dp_countBits(self, num: int) -> list:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i - 1] + 1

        return dp


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            num = int(line)

            ret = Solution().dp_countBits(num)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
