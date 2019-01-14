# coding: utf-8
# 三节点反转链表


def ReverseList(pHead):
    if pHead is None or pHead.next is None:
        return pHead
    node = pHead
    pre_node = None
    while node:
        if node.next is None:
            end_node = node

        next_node = node.next  # 保留next
        node.next = pre_node  # 其实只调整了一个，下一个节点留给下一个循环

        pre_node = node  # 保留当前节点
        node = next_node

    return end_node