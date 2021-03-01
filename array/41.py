# -*- coding: utf-8 -*-
# !@time: 2021-01-06 18:05:02
# !@author: superMC @email: 18758266469@163.com
# !@question title: first-missing-positive

# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,2,0]
# 输出: 3
#  
# 
#  示例 2: 
# 
#  输入: [3,4,-1,1]
# 输出: 2
#  
# 
#  示例 3: 
# 
#  输入: [7,8,9,11,12]
# 输出: 1
#  
# 
#  
# 
#  提示： 
# 
#  你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。 
#  Related Topics 数组 
#  👍 908 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for a in nums:  # 遍历每个座位，记当前坐着a号乘客
            while 0 < a <= len(nums) and a != nums[a - 1]:  # 乘客a是正票但坐错了! 其座位被 ta=nums[a-1]占了
                nums[a - 1], a = a, nums[a - 1]  # a和ta两人互换则a对号入座。此后ta相当于新的a，去找自己的座位（循环执行）
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1  # 找到首个没有对号入座的nums[i]!=i+1
        return len(nums) + 1  # 满座，返回N+1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [7, 8, 9, 11, 12]
    ret = Solution().firstMissingPositive(nums)
    print(ret)
