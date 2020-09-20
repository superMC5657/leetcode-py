# -*- coding: utf-8 -*-
# 2020-09-18 10:03:30
# !@author: superMC @email: 18758266469@163.com
# !@title: robot-in-a-grid-lcci.py

# 设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角
# 移动到右下角的路径。 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。 
# 
#  示例 1: 
# 
#  输入:
# [
#    [0,0,0],
#    [0,1,0],
#    [0,0,0]
# ]
# 输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
# 解释: 
# 输入中标粗的位置即为输出表示的路径，即
# 0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角） 
# 
#  说明：r 和 c 的值均不超过 100。 
#  Related Topics 动态规划 
#  👍 31 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        ans, r, c = [], len(obstacleGrid), len(obstacleGrid[0])

        def f(path):
            if not ans:
                i, j = path[-1]
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 1
                    i < r - 1 and f(path + [[i + 1, j]])
                    j < c - 1 and f(path + [[i, j + 1]])
                    if (i, j) == (r - 1, c - 1):
                        ans.extend(path)

        f([[0, 0]])
        return ans



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    obstacle_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    ret = solution.pathWithObstacles(obstacle_grid)
    print(ret)