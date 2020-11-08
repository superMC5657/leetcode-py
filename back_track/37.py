# -*- coding: utf-8 -*-
# !@time: 2020-11-07 20:32:09
# !@author: superMC @email: 18758266469@163.com
# !@question title: sudoku-solver

# 编写一个程序，通过填充空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  提示： 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法 
#  👍 680 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        palace = [[set() for _ in range(3)] for _ in range(3)]  # 3*3
        blank = []

        # 初始化，按照行、列、宫 分别存入哈希表
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    blank.append((i, j))
                else:
                    row[i].add(ch)
                    col[j].add(ch)
                    palace[i // 3][j // 3].add(ch)

        def dfs(n):
            if n == len(blank):
                return True
            i, j = blank[n]
            rst = nums - row[i] - col[j] - palace[i // 3][j // 3]  # 剩余的数字
            ### rst = nums - (row[i] | col[j] | palace[i//3][j//3])
            if not rst:
                return False
            for num in rst:
                board[i][j] = num
                row[i].add(num)
                col[j].add(num)
                palace[i // 3][j // 3].add(num)
                if dfs(n + 1):
                    return True
                row[i].remove(num)
                col[j].remove(num)
                palace[i // 3][j // 3].remove(num)

        dfs(0)
# leetcode submit region end(Prohibit modification and deletion)
