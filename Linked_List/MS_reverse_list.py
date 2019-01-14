# coding: utf-8
# 递归实现链表反转


def ReverseList(self, pHead):
    node = pHead
    if pHead is None or pHead.next is None:  # 1
        return pHead  # 2
    end_node = self.ReverseList(node.next)  # 3
    node.next.next = node  # 4
    node.next = None  # 5
    return end_node  # 6
