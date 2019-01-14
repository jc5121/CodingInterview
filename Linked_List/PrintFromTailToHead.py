# -*- coding:utf-8 -*-
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。


def printListFromTailToHead(listNode):
    if listNode is None:
        return []

    l = list()
    node = listNode
    while node:
        l.insert(0, node.val)
        node = node.next
    return l