# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 合并两个排好序的链表


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
                # write code here
        pMergeHead = pHead1
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                if pHead1.next and pHead1.next.val >= pHead2.val:  # 条件考虑完备
                    pHead1_next = pHead1.next
                    pHead2_next = pHead2.next
                    pHead1.next = pHead2
                    pHead2.next = pHead1_next
                    pHead1 = pHead1_next
                    pHead2 = pHead2_next
                elif pHead1.next is None:
                    pHead1.next = pHead2
                    break
                else:
                    pHead1 = pHead1.next
            else:
                pHead2 = pHead2.next
        return pMergeHead