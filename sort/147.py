# -*- coding: utf-8 -*-
# 2020-11-20 00:22:07
# !@author: superMC @email: 18758266469@163.com
# !@title: insertion-sort-list.py

# 对链表进行插入排序。 
# 
#  
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。 
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。 
# 
#  
# 
#  插入排序算法： 
# 
#  
#  插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。 
#  每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。 
#  重复直到所有输入数据插入完为止。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#  
# 
#  示例 2： 
# 
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#  
#  Related Topics 排序 链表 
#  👍 235 👎 0

from typing import List
from tools.utils import createListNode, printListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList_self(self, head: ListNode) -> ListNode:
        if not head:
            return None
        n_head = head.next
        head.next = None

        while n_head:
            tmp = n_head.next
            n_head.next = None
            if n_head.val < head.val:
                n_head.next = head
                head = n_head
            else:
                tmp_2 = head.next
                last_tmp_2 = head
                while tmp_2:
                    if n_head.val < tmp_2.val:
                        n_head.next = tmp_2
                        last_tmp_2.next = n_head
                        break
                    else:
                        last_tmp_2 = tmp_2
                        tmp_2 = tmp_2.next
                else:
                    last_tmp_2.next = n_head

            n_head = tmp
        return head

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next

        return dummyHead.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    l = [-1, 5, 3, 4, 0]
    head = createListNode(ListNode, l)
    head = Solution().insertionSortList(head)
    ret = printListNode(head)
    print(ret)
