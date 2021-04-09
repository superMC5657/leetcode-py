# -*- coding: utf-8 -*-
# !@time: 2021-04-09 21:00:56	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: find-minimum-in-rotated-sorted-array-ii.py

# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变
# 化后可能得到：
#  
#  若旋转 4 次，则可以得到 [4,5,6,7,0,1,4] 
#  若旋转 7 次，则可以得到 [0,1,4,4,5,6,7] 
#  
# 
#  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], 
# ..., a[n-2]] 。 
# 
#  给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,5]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,0,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 5000 
#  -5000 <= nums[i] <= 5000 
#  nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。 
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 
#  
#  Related Topics 数组 二分查找 
#  👍 323 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] < nums[r] or l == r:
                return nums[l]
            elif nums[l] > nums[r]:
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            else:
                r = r - 1


# leetcode submit region end(Prohibit modification and deletion)
nums = [10, 1, 10, 10, 10]
ret = Solution().findMin(nums)
print(ret)
