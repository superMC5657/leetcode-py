# -*- coding: utf-8 -*-
# !@time: 2021-03-03 13:05:05
# !@author: superMC @email: 18758266469@163.com
# !@question title: knight-probability-in-chessboard

# 已知一个 NxN 的国际象棋棋盘，棋盘的行号和列号都是从 0 开始。即最左上角的格子记为 (0, 0)，最右下角的记为 (N-1, N-1)。 
# 
#  现有一个 “马”（也译作 “骑士”）位于 (r, c) ，并打算进行 K 次移动。 
# 
#  如下图所示，国际象棋的 “马” 每一步先沿水平或垂直方向移动 2 个格子，然后向与之相垂直的方向再移动 1 个格子，共有 8 个可选的位置。 
# 
#  
# 
#  
# 
#  
# 
#  现在 “马” 每一步都从可选的位置（包括棋盘外部的）中独立随机地选择一个进行移动，直到移动了 K 次或跳到了棋盘外面。 
# 
#  求移动结束后，“马” 仍留在棋盘上的概率。 
# 
#  
# 
#  示例： 
# 
#  输入: 3, 2, 0, 0
# 输出: 0.0625
# 解释: 
# 输入的数据依次为 N, K, r, c
# 第 1 步时，有且只有 2 种走法令 “马” 可以留在棋盘上（跳到（1,2）或（2,1））。对于以上的两种情况，各自在第2步均有且只有2种走法令 “马” 仍
# 然留在棋盘上。
# 所以 “马” 在结束后仍在棋盘上的概率为 0.0625。
#  
# 
#  
# 
#  注意： 
# 
#  
#  N 的取值范围为 [1, 25] 
#  K 的取值范围为 [0, 100] 
#  开始时，“马” 总是位于棋盘上 
#  
#  Related Topics 动态规划 
#  👍 102 👎 0
import functools
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def knightProbability_cache(self, N: int, K: int, r: int, c: int) -> float:
        @functools.lru_cache(None)
        def dfs(r, c, K):

            if r < 0 or r > N - 1 or c < 0 or c > N - 1:
                return 0
            if K == 0:
                return 1

            step = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

            res = 0

            for i, j in step:
                res += dfs(r + i, c + j, K - 1)

            return res / 8

        return dfs(r, c, K)

    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2, 1), (2, -1), (-2, 1), (-2, -1),
                                   (1, 2), (1, -2), (-1, 2), (-1, -2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r + dr][c + dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    N, K, r, c = 3, 2, 0, 0
    res = Solution().knightProbability(N, K, r, c)
    print(res)
