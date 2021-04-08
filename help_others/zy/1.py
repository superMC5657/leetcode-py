# -*- coding: utf-8 -*-
# !@time: 2021/4/8 2:51 下午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 1.py

# 给定一棵二叉搜索树，请找出其中第k大的节点。
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4

# Definition for a binary tree node.
from tools.utils import createtree


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = [5, 3, 6, 2, 4, None, None, 1]
k = 3
root = createtree(TreeNode, root)


def find_topk(root, k):
    if root is None:
        return None
    l = []

    def midsearch(root):
        if root:
            midsearch(root.right)
            l.append(root.val)
            midsearch(root.left)

    midsearch(root)
    return l[k - 1]


ret = find_topk(root, k)
print(ret)
