# 给定一个二进制数组， 计算其中最大连续1的个数。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#  
# 
#  注意： 
# 
#  
#  输入的数组只包含 0 和1。 
#  输入数组的长度是正整数，且不超过 10,000。 
#  
#  Related Topics 数组 
#  👍 184 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1_len = 0
        _1_len = 0
        flag_1 = 0
        for index, num in enumerate(nums):
            if num == 1:
                if flag_1 == 1:
                    _1_len += 1
                else:
                    _1_len = 1
                    flag_1 = 1
                max_1_len = max(_1_len, max_1_len)
            else:
                flag_1 = 0
        return max_1_len


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ret = Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    print(ret)
