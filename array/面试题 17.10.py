# -*- coding: utf-8 -*-
# !@time: 2021-07-09 01:23:54	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: find-majority-element-lcci.py

# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1
# ) 的解决方案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[1,2,5,9,5,9,5,5,5]
# 输出：5 
# 
#  示例 2： 
# 
#  
# 输入：[3,2]
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：[2,2,1,1,1,2,2]
# 输出：2 
#  Related Topics 数组 计数 
#  👍 89 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_d = dict()
        for num in nums:
            if num in n_d:
                n_d[num] += 1
            else:
                n_d[num] = 1
        for k, v in n_d.items():
            if v > len(nums) / 2:
                return k
        else:
            return -1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [3, 2]
    print(Solution().majorityElement(nums))
