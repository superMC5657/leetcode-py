# -*- coding: utf-8 -*-
# !@time: 2021-04-17 00:19:31	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: contains-duplicate-iii.py

# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在两个下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，
# 同时又满足 abs(i - j) <= k 。 
# 
#  如果存在则返回 true，不存在返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 2 * 104 
#  -231 <= nums[i] <= 231 - 1 
#  0 <= k <= 104 
#  0 <= t <= 231 - 1 
#  
#  Related Topics 排序 Ordered Map 
#  👍 316 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyAlmostDuplicate_violence(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(0, len(nums) - 1):
            right = min(i + k + 1, len(nums))
            for j in range(i + 1, right):
                if abs(nums[j] - nums[i]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        all_buckets = {}
        bucket_size = t + 1
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size  # 放入哪个桶

            if bucket_num in all_buckets:  # 桶中已经有元素了
                return True

            all_buckets[bucket_num] = nums[i]  # 把nums[i]放入桶中

            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:  # 检查前一个桶
                return True

            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:  # 检查后一个桶
                return True

            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i - k] // bucket_size)

        return False


# leetcode submit region end(Prohibit modification and deletion)
nums = [1, 2, 3, 1]
k = 3
t = 0
ret = Solution().containsNearbyAlmostDuplicate(nums, k, t)
print(ret)
