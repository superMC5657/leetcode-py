# -*- coding: utf-8 -*-
# !@time: 2020-06-07 01:04
# !@author: superMC @email: 18758266469@163.com
# !@fileName: rebuild_binary_tree.py


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        if i > 0:
            root.left = self.reConstructBinaryTree(pre[1:1 + i], tin[:i])
        if i < len(tin) - 1:
            root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root
