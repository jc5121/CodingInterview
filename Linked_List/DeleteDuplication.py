# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None
        pResHead = ListNode(pHead.val - 1)
        tempResHead = pResHead
        same = pHead.val - 1
        p = pHead
        while p != None:
            if p.val == same:
                pass
                p = p.next
            else:
                same = p.val
                if p.next == None or p.val != p.next.val:  # 只有这种情况才移动，考虑了None
                    tempResHead.next = p
                    tempResHead = tempResHead.next  # temp只是别名,理解为指针
                    p = p.next
        tempResHead.next = None
        return pResHead.next
