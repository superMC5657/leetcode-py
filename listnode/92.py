# -*- coding: utf-8 -*-
# !@time: 2021-03-18 16:30:54
# !@author: superMC @email: 18758266469@163.com
# !@question title: reverse-linked-list-ii

# 给你单链表的头节点 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目为 n 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# 
#  进阶： 你可以使用一趟扫描完成反转吗？ 
#  Related Topics 链表 
#  👍 784 👎 0
from tools.utils import createListNode, printListNode
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(-1)  # 可以省略很多讨论
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(left, right):
            next = cur.next  # 选择下一个节点
            cur.next = next.next  # 连接右边的节点
            next.next = pre.next  # 指向左边的一个
            pre.next = next  # pre 指向当前节点

        return dummy_node.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    head = createListNode(ListNode, head)
    head = Solution().reverseBetween(head, left, right)
    printListNode(head)
