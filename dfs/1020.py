# -*- coding: utf-8 -*-
# !@time: 2020-10-20 14:41:27
# !@author: superMC @email: 18758266469@163.com
# !@question title: number-of-enclaves

# 给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。 
# 
#  移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。 
# 
#  返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释： 
# 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。 
# 
#  示例 2： 
# 
#  输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：
# 所有 1 都在边界上或可以到达边界。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 500 
#  1 <= A[i].length <= 500 
#  0 <= A[i][j] <= 1 
#  所有行的大小都相同 
#  
#  Related Topics 深度优先搜索 
#  👍 38 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])

        def dfs(i, j):
            A[i][j] = 0
            border_around = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for x, y in border_around:
                if 0 <= x <= m - 1 and 0 <= y <= n - 1:
                    if A[x][y] == 1:
                        dfs(x, y)

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if A[i][j] == 1:
                        dfs(i, j)
        s = sum(map(sum, A))
        return s


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    A = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    ret = Solution().numEnclaves(A)
    print(ret)
