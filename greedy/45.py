# -*- coding: utf-8 -*-
# !@time: 2021-04-05 05:11:22	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: jump-game-ii.py

# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组 
#  👍 899 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        if nums[0] >= nums_len - 1:
            return 1
        step = 1
        loc = 0
        while loc < nums_len:
            max_pos = 0
            next = 0
            for i in range(1, nums[loc] + 1):
                cache_next = loc + i
                if nums[cache_next] + cache_next > max_pos:
                    next = cache_next
                    max_pos = nums[cache_next] + cache_next
                    if max_pos >= nums_len - 1:
                        return step + 1
            loc = next
            step += 1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ret = Solution().jump([1, 2, 3, 4])
    print(ret)
