# -*- coding: utf-8 -*-
# 2020-09-27 00:45:52
# !@author: superMC @email: 18758266469@163.com
# !@title: maximal-square.py

# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。 
# 
#  示例: 
# 
#  输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4 
#  Related Topics 动态规划 
#  👍 569 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(m)]

        max_edge = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    # boundary
                    if matrix[i][j] == '1':
                        dp[i][j] = 1
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = 1
                        if dp[i - 1][j] and dp[i][j - 1]:
                            dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                max_edge = max(dp[i][j], max_edge)
        return max_edge ** 2


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    matrix = [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"],
              ["0", "1", "1", "1"]]
    ret = Solution().maximalSquare(matrix)
    print(ret)
