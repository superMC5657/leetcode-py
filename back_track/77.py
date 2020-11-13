# -*- coding: utf-8 -*-
# !@time: 2020-11-13 14:58:41
# !@author: superMC @email: 18758266469@163.com
# !@question title: combinations

# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 434 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def get_k_num(base, index, n_, k_):
            for i in range(index, n_ - k_ + 2):
                base_copy = base.copy()
                base_copy.append(i)
                if k_ == 1:
                    ret.append(base_copy)
                else:
                    get_k_num(base_copy, i + 1, n_, k_ - 1)

        get_k_num([], 1, n, k)
        return ret


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ret = Solution().combine(4, 2)
    print(ret)
