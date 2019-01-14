# coding: utf-8
# O(1)时间内删除给定链表节点


def deleteNode(pToBeDeleted):
    # 是否为为节点
    if pToBeDeleted.next is None:
        pToBeDeleted = None
    else:
        pToBeDeleted.val = pToBeDeleted.next.val
        pToBeDeleted.next = pToBeDeleted.next.next