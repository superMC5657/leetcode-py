# -*- coding: utf-8 -*-
# !@time: 2021-04-03 04:09:42
# !@author: superMC @email: 18758266469@163.com
# !@question title: knight-dialer

# 国际象棋中的骑士可以按下图所示进行移动： 
# 
#  . 
# 
#  
# 这一次，我们将 “骑士” 放在电话拨号盘的任意数字键（如上图所示）上，接下来，骑士将会跳 N-1 步。每一步必须是从一个数字键跳到另一个数字键。 
# 
#  每当它落在一个键上（包括骑士的初始位置），都会拨出键所对应的数字，总共按下 N 位数字。 
# 
#  你能用这种方式拨出多少个不同的号码？ 
# 
#  因为答案可能很大，所以输出答案模 10^9 + 7。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：1
# 输出：10
#  
# 
#  示例 2： 
# 
#  输入：2
# 输出：20
#  
# 
#  示例 3： 
# 
#  输入：3
# 输出：46
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 5000 
#  
#  Related Topics 动态规划 
#  👍 72 👎 0
from copy import copy
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from copy import copy


class Solution:
    def __init__(self):
        self.dialer = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3],
                       9: [2, 4]
                       }

    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        sums_pre = [1] * 10
        for i in range(1, n):
            sums_now = [0] * 10
            for k, v in self.dialer.items():
                for s in v:
                    sums_now[k] += sums_pre[s] % mod
            sums_pre = sums_now
        return sum(sums_pre) % mod


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().knightDialer(3))
