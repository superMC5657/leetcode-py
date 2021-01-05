# -*- coding: utf-8 -*-
# !@time: 2020-12-01 16:35:46
# !@author: superMC @email: 18758266469@163.com
# !@question title: find-first-and-last-position-of-element-in-sorted-array

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  nums 是一个非递减数组 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 二分查找 
#  👍 726 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2  # 向左取整
            if nums[mid] < target:  # 首先考虑一定不存在解的区间，则有+1（或者-1）
                l = mid + 1
            else:
                r = mid
        if not nums or nums[l] != target:  # 用例中有nums = [] 的情况
            return res
        res[0] = l

        l, r = r, len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2  # 向右取整
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        res[1] = r
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 6

    ret = Solution().searchRange(nums, target)
    print(ret)
