# -*- coding: utf-8 -*-
# !@time: 2020/8/26 3:30 上午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 464.py
"""
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定一个整数"maxChoosableInteger"（整数池中可选择的最大数）和另一个整数"desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？

你可以假设"maxChoosableInteger"不会大于 20，"desiredTotal"不会大于 300。

"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        import functools
        if desiredTotal <= maxChoosableInteger: return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal: return False

        @functools.lru_cache(None)
        def dfs(used, desiredTotal):
            for i in range(maxChoosableInteger):
                cur = 1 << i
                if cur & used == 0:
                    if desiredTotal <= i + 1 or not dfs(cur | used, desiredTotal - i - 1):
                        return True
            return False

        return dfs(0, desiredTotal)


if __name__ == '__main__':
    result = Solution().canIWin(20, 100)
    print(result)
