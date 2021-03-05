# -*- coding: utf-8 -*-
# !@time: 2021-03-04 01:17:02	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: russian-doll-envelopes.py

# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如
# 同俄罗斯套娃一样。 
# 
#  请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。 
# 
#  说明: 
# 不允许旋转信封。 
# 
#  示例: 
# 
#  输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3 
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
#  
#  Related Topics 二分查找 动态规划 
#  👍 292 👎 0
import bisect
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num

        return len(f)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    ret = Solution().maxEnvelopes(envelopes)
    print(envelopes)
