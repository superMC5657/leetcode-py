# -*- coding: utf-8 -*-
# !@time: 2021-03-16 00:20:47	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: spiral-matrix-ii.py

# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
#  Related Topics 数组 
#  👍 321 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        total = n * n
        rows = cols = n
        matrix = [[0] * cols for _ in range(rows)]
        visited = [[False] * cols for _ in range(rows)]
        order = [0] * total
        for i in range(total):
            order[i] = i + 1

        row = col = 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0

        for i in range(total):
            matrix[row][col] = order[i]
            visited[row][col] = True
            nextRow, nextCol = row + direction[directionIndex][0], col + direction[directionIndex][1]
            if not (nextRow in range(rows) and nextCol in range(cols) and not visited[nextRow][nextCol]):
                directionIndex = (directionIndex + 1) % 4
            row += direction[directionIndex][0]
            col += direction[directionIndex][1]
        return matrix

# leetcode submit region end(Prohibit modification and deletion)
