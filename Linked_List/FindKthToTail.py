# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None
        forward_node = head
        behind_node = head

        for i in range(k - 1):  # 链表长度小于k
            if forward_node.next is None:
                return None
            else:
                forward_node = forward_node.next

        while forward_node.next:
            forward_node = forward_node.next
            behind_node = behind_node.next
        return behind_node