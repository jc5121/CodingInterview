# -*- coding:utf-8 -*-


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        pFast = pHead
        pSlow = pHead
        while pFast.next is not None:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                break
        if pFast.next is None:
            return None

        pSlow = pHead
        while pFast != pSlow:  # 第二次相遇一定就是入口，画图，three棒棒的～
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast
