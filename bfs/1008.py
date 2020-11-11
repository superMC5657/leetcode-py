# -*- coding: utf-8 -*-
# !@time: 2020-10-13 21:49:51
# !@author: superMC @email: 18758266469@163.com
# !@question title: construct-binary-search-tree-from-preorder-traversal

# 返回与给定前序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。 
# 
#  (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right
#  的任何后代，值总 > node.val。此外，前序遍历首先显示节点 node 的值，然后遍历 node.left，接着遍历 node.right。） 
# 
#  题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。 
# 
#  
# 
#  示例： 
# 
#  输入：[8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= preorder.length <= 100 
#  1 <= preorder[i] <= 10^8 
#  preorder 中的值互不相同 
#  
#  Related Topics 树 
#  👍 108 👎 0
import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> List:
        if not preorder:
            return None
        root = TreeNode(val=preorder[0])

        def construct(root, value):
            if value < root.val:
                if not root.left:
                    root.left = TreeNode(value)
                else:
                    construct(root.left, value)
            else:
                if not root.right:
                    root.right = TreeNode(value)
                else:
                    construct(root.right, value)

        for value in preorder[1:]:
            construct(root, value)
        return self.sequence_compilation(root)

    def sequence_compilation(self, root):
        if not root:
            return []
        queue = collections.deque()  # 维护要打印的行
        ret = []
        queue.append(root)
        while queue:
            if queue.count('null') == queue.__len__():
                break
            node = queue.popleft()
            if node == 'null':
                ret.append('null')
                continue
            ret.append(node.val)
            if node.left:
                queue.append(node.left)
            else:
                queue.append('null')
            if node.right:
                queue.append(node.right)
            else:
                queue.append('null')

        return ret


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ret = Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])
    print(ret)
