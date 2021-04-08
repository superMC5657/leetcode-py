# -*- coding: utf-8 -*-
# !@time: 2021-04-08 14:56:26	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: kth-smallest-element-in-a-bst.py

# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数为 n 。 
#  1 <= k <= n <= 104 
#  0 <= Node.val <= 104 
#  
# 
#  
# 
#  进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？ 
#  Related Topics 树 二分查找 
#  👍 376 👎 0


from typing import List
from tools.utils import createtree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# from tools.utils import createtree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = [5, 3, 6, 2, 4, None, None, 1]
    k = 3
    root = createtree(TreeNode, root)
    ret = Solution().kthSmallest(root, k)
    print(ret)
