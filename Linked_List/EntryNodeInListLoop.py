# -*- coding:utf-8 -*-
# 解释：设slow走到相遇点走了k步，倒退a步走到入口节点，
# fast第一次走到这里也是k步，（走了2k-k=k之后还是这个点），
# 所以再走k步也一定还是到相遇点，那么再走k-a步就是入口点，
# slow走k-a步也是入口点，所以可以直接相遇来判断入口点



class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        pFast = pHead
        pSlow = pHead
        while pFast.next is not None:
            pFast = pFast.next.next  # slow *2 == fast
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
