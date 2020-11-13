# -*- coding: utf-8 -*-
# 2020-10-18 09:06:22
# !@author: superMC @email: 18758266469@163.com
# !@title: flatten-binary-tree-to-linked-list.py

# 给定一个二叉树，原地将它展开为一个单链表。 
# 
#  
# 
#  例如，给定二叉树 
# 
#      1
#    / \
#   2   5
#  / \   \
# 3   4   6 
# 
#  将其展开为： 
# 
#  1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6 
#  Related Topics 树 深度优先搜索 
#  👍 593 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 先序排列
        if not root:
            return
        cache = []

        def preoder(root):
            cache.append(root)
            if root.left:
                preoder(root.left)
            if root.right:
                preoder(root.right)

        preoder(root)
        for i in range(len(cache) - 1):
            cache[i].left = None
            cache[i].right = cache[i + 1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    from tools.utils import createtree

    root = createtree(TreeNode, [1, 2, 5, 3, 4, None, 6])
    Solution().flatten(root)
    print(root)
