# -*- coding: utf-8 -*-
# !@time: 2021-03-01 18:00:05
# !@author: superMC @email: 18758266469@163.com
# !@question title: range-sum-query-immutable

# 给定一个整数数组 nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。 
# 
#  
#  
#  实现 NumArray 类： 
# 
#  
#  NumArray(int[] nums) 使用数组 nums 初始化对象 
#  int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 s
# um(nums[i], nums[i + 1], ... , nums[j])） 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# 输出：
# [null, 1, -1, -3]
# 
# 解释：
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 104 
#  -105 <= nums[i] <= 105 
#  0 <= i <= j < nums.length 
#  最多调用 104 次 sumRange 方法 
#  
#  
#  
#  Related Topics 动态规划 
#  👍 280 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:

    def __init__(self, nums: List[int]):
        sums = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            sums[i + 1] = sums[i] + num
        self.sums = sums

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print(na.sums)
    print(na.sumRange(0, 2))
