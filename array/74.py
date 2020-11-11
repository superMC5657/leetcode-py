# -*- coding: utf-8 -*-
# !@time: 2020-11-08 15:23:15
# !@author: superMC @email: 18758266469@163.com
# !@question title: search-a-2d-matrix

# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [], target = 0
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  0 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics 数组 二分查找 
#  👍 273 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        size = m * n
        low = 0
        high = size
        while low < high:
            index = (low + high) // 2
            index_x, index_y = divmod(index, n)
            if index == low or index == high:
                index = low = high
            if matrix[index_x][index_y] == target:
                return True
            elif matrix[index_x][index_y] < target:
                low = index
            else:
                high = index
        return False
    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    matrix = [[1]]
    target = 1
    ret = Solution().searchMatrix(matrix, target)
    print(ret)
