# -*- coding: utf-8 -*-
# !@time: 2021-02-12 00:29:41	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: pascals-triangle-ii.py

# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 3
# 输出: [1,3,3,1]
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(k) 空间复杂度吗？ 
#  Related Topics 数组 
#  👍 224 👎 0
from copy import deepcopy
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row_list = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row_list[j] += row_list[j - 1]

        return row_list


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    r_l = Solution().getRow(3)
    print(r_l)
