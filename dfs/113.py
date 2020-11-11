# -*- coding: utf-8 -*-
# !@time: 2020-11-01 20:43:40
# !@author: superMC @email: 18758266469@163.com
# !@question title: path-sum-ii

# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
#  Related Topics 树 深度优先搜索 
#  👍 375 👎 0

from typing import List

from tools.utils import createtree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ret_list = []

        def dfs(node, sub_sum, l):
            sub_sum = sub_sum + node.val

            if node:
                new_l = l.copy()
                new_l.append(node.val)
                if node.left:
                    dfs(node.left, sub_sum, new_l)
                if node.right:
                    dfs(node.right, sub_sum, new_l)
                if not node.right and not node.left:
                    if sub_sum == sum:
                        ret_list.append(new_l)

        dfs(root, 0, [])
        return ret_list


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = createtree(TreeNode, [-2, None, -3])
    ret = Solution().pathSum(root, -5)
    print(ret)
