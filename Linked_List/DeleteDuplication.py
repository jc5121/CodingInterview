# -*- coding:utf-8 -*-
# 删除链表中重复的节点
# 这种题我为什么反而觉得难？


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None
        # 增加头部
        pResHead = ListNode(pHead.val - 1)  # 返回的链表头
        tempResHead = pResHead  # 用来记录当前最后一个不重复的node
        same = pHead.val - 1
        p = pHead  # 当前node
        while p != None:
            if p.val == same:
                pass  # 不用直接删除，先往后走就可以
                p = p.next
            else:
                same = p.val
                if p.next == None or p.val != p.next.val:  # 只有这种情况才移动，考虑了None
                    tempResHead.next = p
                    tempResHead = tempResHead.next  # temp只是别名,理解为指针
                    p = p.next
        tempResHead.next = None
        return pResHead.next
