# -*- coding: utf-8 -*-
# !@time: 2021-07-05 23:02:40
# !@author: superMC @email: 18758266469@163.com
# !@question title: merge-intervals

# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 104 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 104 
#  
#  Related Topics 数组 排序 
#  👍 990 👎 0
import sys
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals):
        ret = []
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                ret.append([start, end])
                start = intervals[i][0]
            end = max(end, intervals[i][1])
        ret.append([start, end])
        return ret


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    intervals = [[1,4],[2,3]]
    print(Solution().merge(intervals))
