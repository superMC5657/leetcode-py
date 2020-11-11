# -*- coding: utf-8 -*-
# !@time: 2020-10-31 18:05:37
# !@author: superMC @email: 18758266469@163.com
# !@question title: search-in-rotated-sorted-array

# 给你一个升序排列的整数数组 nums ，和一个整数 target 。 
# 
#  假设按照升序排序的数组在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。 
# 
#  请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1], target = 0
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -10^4 <= nums[i] <= 10^4 
#  nums 中的每个值都 独一无二 
#  nums 肯定会在某个点上旋转 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 二分查找 
#  👍 1043 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
# leetcode submit region end(Prohibit modification and deletion)

