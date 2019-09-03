# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return
        p1 = pHead1
        p2 = pHead2

        # 此时p1,p2中有一个还没走完，剩下的就是它俩相差的
        while p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next
        temphead1 = pHead1
        temphead2 = pHead2

        # 先走了n步
        while p1.next:
            temphead1 = temphead1.next
            p1 = p1.next
        while p2.next:
            temphead2 = temphead2.next
            p2 = p2.next
        while temphead1:
            if temphead1 == temphead2:
                return temphead1
            else:
                temphead1 = temphead1.next
                temphead2 = temphead2.next
