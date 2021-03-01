# -*- coding: utf-8 -*-
# !@time: 2021-02-25 17:28:52	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: transpose-matrix.py

# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。 
# 
#  矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 1000 
#  1 <= m * n <= 105 
#  -109 <= matrix[i][j] <= 109 
#  
#  Related Topics 数组 
#  👍 174 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        new_matrix = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix
# leetcode submit region end(Prohibit modification and deletion)
