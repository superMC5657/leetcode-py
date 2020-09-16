# -*- coding: utf-8 -*-
# !@time: 2020-09-15 17:18:24
# !@author: superMC @email: 18758266469@163.com
# !@question title: rotate-image

# 给定一个 n × n 的二维矩阵表示一个图像。 
# 
#  将图像顺时针旋转 90 度。 
# 
#  说明： 
# 
#  你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。 
# 
#  示例 1: 
# 
#  给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#  
# 
#  示例 2: 
# 
#  给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 
# 
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
#  
#  Related Topics 数组 
#  👍 560 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix[0])
        # # transpose matrix
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        #
        #         # reverse each row
        # for i in range(n):
        #     matrix[i].reverse()

        matrix[:] = zip(*matrix[::-1])

# leetcode submit region end(Prohibit modification and deletion)
