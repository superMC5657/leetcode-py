# -*- coding: utf-8 -*-
# !@time: 2021-03-27 19:14:58
# !@author: superMC @email: 18758266469@163.com
# !@question title: rotate-list

# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 500] 内 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 109 
#  
#  Related Topics 链表 双指针 
#  👍 513 👎 0

from typing import List
from tools.utils import createListNode, printListNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        list_node_len = 1
        c_head = head
        while c_head.next:
            list_node_len += 1
            c_head = c_head.next
        c_head.next = head
        k = k % list_node_len
        k_c = list_node_len - k
        for i in range(k_c - 1):
            head = head.next
        pre_head = head
        head = head.next
        pre_head.next = None
        return head
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    k = 2
    head = createListNode(ListNode, head)
    ret = Solution().rotateRight(head, k)
    printListNode(ret)
