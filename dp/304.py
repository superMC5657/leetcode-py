# -*- coding: utf-8 -*-
# !@time: 2021-03-02 12:21:04
# !@author: superMC @email: 18758266469@163.com
# !@question title: range-sum-query-2d-immutable

# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。 
# 
#  
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。 
# 
#  
# 
#  示例： 
# 
#  
# 给定 matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#  
# 
#  
# 
#  提示： 
# 0
#  
#  你可以假设矩阵不可变。 
#  会多次调用 sumRegion 方法。 
#  你可以假设 row1 ≤ row2 且 col1 ≤ col2 。 
#  
#  Related Topics 动态规划 
#  👍 186 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] + matrix[i][j] - dp[i][j]
        self.dp = dp
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.dp
        # 考虑到边界条件row1与col1两条线上的element不能被减去所以当使用row1,与col１时应该减去一．

        return _sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + _sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
row1, col1, row2, col2 = [2, 1, 4, 3]
nm = NumMatrix(matrix)
param_1 = nm.sumRegion(row1, col1, row2, col2)
print(param_1)
