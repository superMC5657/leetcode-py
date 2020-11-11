# -*- coding: utf-8 -*-
# !@time: 2020-11-03 21:20:36
# !@author: superMC @email: 18758266469@163.com
# !@question title: find-the-duplicate-number

# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出
# 这个重复的数。 
# 
#  示例 1: 
# 
#  输入: [1,3,4,2,2]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [3,1,3,4,2]
# 输出: 3
#  
# 
#  说明： 
# 
#  
#  不能更改原数组（假设数组是只读的）。 
#  只能使用额外的 O(1) 的空间。 
#  时间复杂度小于 O(n2) 。 
#  数组中只有一个重复的数字，但它可能不止重复出现一次。 
#  
#  Related Topics 数组 双指针 二分查找 
#  👍 941 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        slow_index = 0
        fast_index = 0
        finder_index = 0
        while True:
            slow_index = nums[slow_index]
            fast_index = nums[nums[fast_index]]
            if fast_index == slow_index:
                break
        while True:
            finder_index = nums[finder_index]
            slow_index = nums[slow_index]
            if finder_index == slow_index:
                break

        return slow_index


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    ret = Solution().findDuplicate(nums)
    print(ret)
