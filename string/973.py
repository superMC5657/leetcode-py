# -*- coding: utf-8 -*-
# !@time: 2020-11-09 19:55:06
# !@author: superMC @email: 18758266469@163.com
# !@question title: k-closest-points-to-origin

# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。 
# 
#  （这里，平面上两点之间的距离是欧几里德距离。） 
# 
#  你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：points = [[1,3],[-2,2]], K = 1
# 输出：[[-2,2]]
# 解释： 
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
#  
# 
#  示例 2： 
# 
#  输入：points = [[3,3],[5,-1],[-2,4]], K = 2
# 输出：[[3,3],[-2,4]]
# （答案 [[-2,4],[3,3]] 也会被接受。）
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= K <= points.length <= 10000 
#  -10000 < points[i][0] < 10000 
#  -10000 < points[i][1] < 10000 
#  
#  Related Topics 堆 排序 分治算法 
#  👍 182 👎 0
from math import sqrt
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        closest_distance = []
        closest_points = []
        for point in points:
            distance = sqrt(pow(point[0], 2) + pow(point[1], 2))
            closest_distance.append(distance)
        closest_distance_index = sorted(range(len(closest_distance)), key=lambda x: closest_distance[x])
        for i in range(K):
            closest_points.append(points[closest_distance_index[i]])
        return closest_points


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    points = [[1, 3], [-2, 2]]
    K = 1
    ret = Solution().kClosest(points, K)
    print(ret)
