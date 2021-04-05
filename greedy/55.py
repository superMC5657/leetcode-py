# -*- coding: utf-8 -*-
# !@time: 2021-04-05 15:33:13	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: jump-game.py

# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  判断你是否能够到达最后一个下标。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  0 <= nums[i] <= 105 
#  
#  Related Topics 贪心算法 数组 
#  👍 1121 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        last_loc = len(nums) - 1

        for i in range(last_loc - 1, -1, -1):
            if nums[i] + i >= last_loc:
                last_loc = i

        return last_loc == 0


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ret = Solution().canJump(nums)
    print(ret)
