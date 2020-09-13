# -*- coding: utf-8 -*-
# 2020-09-11 02:06:48
# !@author: superMC @email: 18758266469@163.com
# !@title: next-permutation.py

# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。 
# 
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
# 
#  必须原地修改，只允许使用额外常数空间。 
# 
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。 
# 1,2,3 → 1,3,2 
# 3,2,1 → 1,2,3 
# 1,1,5 → 1,5,1 
#  Related Topics 数组 
#  👍 654 👎 0

from typing import List


#

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation_self(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        flag = False
        for i in range(nums_len - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    flag = True
                    break
            if flag:
                break
        if not flag:
            nums.reverse()

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2: return
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                nums[i + 1:] = sorted(nums[i + 1:])
                return
        nums.sort()


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    print(nums)
