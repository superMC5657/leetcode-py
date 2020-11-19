# -*- coding: utf-8 -*-
# 2020-11-19 15:57:38
# !@author: superMC @email: 18758266469@163.com
# !@title: gas-station.py

# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。 
# 
#  你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。 
# 
#  如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。 
# 
#  说明: 
# 
#  
#  如果题目有解，该答案即为唯一答案。 
#  输入数组均为非空数组，且长度相同。 
#  输入数组中的元素均为非负数。 
#  
# 
#  示例 1: 
# 
#  输入: 
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# 
# 输出: 3
# 
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。 
# 
#  示例 2: 
# 
#  输入: 
# gas  = [2,3,4]
# cost = [3,4,3]
# 
# 输出: -1
# 
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。 
#  Related Topics 贪心算法 
#  👍 527 👎 0
import sys
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canCompleteCircuit_violence(self, gas: List[int], cost: List[int]) -> int:
        nums = len(gas)
        for i in range(nums):
            now_gas = 0
            for j in range(nums):
                m = (i + j) % nums
                now_gas += gas[m]
                now_gas -= cost[m]
                if now_gas < 0:
                    break
            else:
                return i
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_cost_sum = 0
        min_index = 0
        for i in range(len(gas)):
            gas_cost_sum += gas[i] - cost[i]
            if i == 0:
                last_min_sum = gas_cost_sum
            if gas_cost_sum < last_min_sum:
                last_min_sum = gas_cost_sum
                min_index = i
        if gas_cost_sum < 0:
            return -1
        else:
            return (min_index + 1) % len(gas)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    gas = [3, 1, 1]
    cost = [1, 2, 2]
    ret = Solution().canCompleteCircuit(gas, cost)
    print(ret)
