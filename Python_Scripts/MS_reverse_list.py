# coding: utf-8
# 递归实现链表反转


def ReverseList(self, pHead):
    node = pHead
    if pHead is None or pHead.next is None:
        return pHead  # 1
    end_node = self.ReverseList(node.next)
    node.next.next = node  # 2
    node.next = None  # 3
    return end_node  # 4
