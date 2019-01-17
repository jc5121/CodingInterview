# coding: utf-8
# 递归实现链表反转


def ReverseList(pHead):
    node = pHead
    if pHead is None or pHead.next is None:  # 1
        return pHead  # 2
    end_node = ReverseList(node.next)  # 3
    node.next.next = node  # 4 真正调整的在这步
    node.next = None  # 5
    return end_node  # 6
