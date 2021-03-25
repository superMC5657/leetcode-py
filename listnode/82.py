# -*- coding: utf-8 -*-
# !@time: 2021-03-25 04:14:03
# !@author: superMC @email: 18758266469@163.com
# !@question title: remove-duplicates-from-sorted-list-ii

# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#  
# 
#  示例 2: 
# 
#  输入: 1->1->1->2->3
# 输出: 2->3 
#  Related Topics 链表 
#  👍 493 👎 0

from typing import List
from tools.utils import createListNode, printListNode
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre_val = -1
        dump = ListNode(pre_val)
        dump.next = head
        cur = dump
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dump.next


# leetcode submit region end(Prohibit modification and deletion)
head = createListNode(ListNode, [1, 2, 3, 3, 4, 4, 5])
head = Solution().deleteDuplicates(head)
printListNode(head)
