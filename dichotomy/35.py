# -*- coding: utf-8 -*-
# !@time: 2020-10-21 20:25:10
# !@author: superMC @email: 18758266469@163.com
# !@question title: search-insert-position

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  你可以假设数组中无重复元素。 
# 
#  示例 1: 
# 
#  输入: [1,3,5,6], 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [1,3,5,6], 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  输入: [1,3,5,6], 7
# 输出: 4
#  
# 
#  示例 4: 
# 
#  输入: [1,3,5,6], 0
# 输出: 0
#  
#  Related Topics 数组 二分查找 
#  👍 722 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        left = 0
        right = nums_len - 1
        index = nums_len // 2
        while True:
            if left == index:
                if nums[left] < target:
                    if nums[right] < target and left != right:
                        return index + 2
                    else:
                        return index + 1
                else:
                    return index
            if nums[index] < target:
                left = index
                index = (left + right) // 2
            elif nums[index] > target:
                right = index
                index = (left + right) // 2
            else:
                return index


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1]
    target = 7
    ret = Solution().searchInsert(nums, target)
    print(ret)
