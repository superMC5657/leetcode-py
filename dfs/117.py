# -*- coding: utf-8 -*-
# !@time: 2020-10-16 13:48:17
# !@author: superMC @email: 18758266469@163.com
# !@question title: populating-next-right-pointers-in-each-node-ii

# 给定一个二叉树 
# 
#  struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL。 
# 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。 
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数小于 6000 
#  -100 <= node.val <= 100 
#  
# 
#  
# 
#  
#  
#  Related Topics 树 深度优先搜索 
#  👍 306 👎 0
import collections
from typing import List


def createtree(l):
    if l[0]:
        root = Node(l[0])
        nodes = [root]
        id = 1
        while nodes and id < len(l):
            node = nodes[0]  # 依次为每个节点分配子节点
            node.left = Node(l[id]) if l[id] else None
            nodes.append(node.left)
            node.right = Node(l[id + 1]) if id < len(l) - 1 and l[id + 1] else None
            nodes.append(node.right)
            id += 2  # 每次取出两个节点
            nodes.pop(0)
        return root
    else:
        return None


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            next_queue = []
            for i in range(len(queue)):
                if queue[i].left:
                    next_queue.append(queue[i].left)
                if queue[i].right:
                    next_queue.append(queue[i].right)
                if i == len(queue) - 1:
                    queue[i].next = None
                else:
                    queue[i].next = queue[i + 1]
            queue = next_queue
        return root


# leetcode submit region end(Prohibit modification and deletion)
l = [1, 2, 3, 4, 5, None, 7]
root = createtree(l)
Solution().connect(root)
