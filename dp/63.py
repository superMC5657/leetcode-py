# -*- coding: utf-8 -*-
# 2020-09-05 04:42:35
# !@author: superMC @email: 18758266469@163.com
# !@title: unique-paths-ii.py

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  说明：m 和 n 的值均不超过 100。 
# 
#  示例 1: 
# 
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
#  Related Topics 数组 动态规划 
#  👍 400 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        store = [[0] * width for i in range(height)]

        # 从上到下，从左到右
        for m in range(height):  # 每一行
            for n in range(width):  # 每一列
                if not obstacleGrid[m][n]:  # 如果这一格没有障碍物
                    if m == n == 0:  # 或if not(m or n)
                        store[m][n] = 1
                    else:
                        a = store[m - 1][n] if m != 0 else 0  # 上方格子
                        b = store[m][n - 1] if n != 0 else 0  # 左方格子
                        store[m][n] = a + b
        return store[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    ret = Solution().uniquePathsWithObstacles([[1]])
    print(ret)
