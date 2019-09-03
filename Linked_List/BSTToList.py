# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 题目： BST -> 双向链表，可以数出来连接数是少了2的
# BST 先中序遍历转化为数组，再转化为双向链表


class Solution:

    # arr = list() 不能写这里
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return None
        self.arr = list()
        self.midTraversal(pRootOfTree)
        for i, v in enumerate(self.arr[:-1]):  # 连接数少2，最后一个节点只添加向前的链，第一个只添加向后的
            v.right = self.arr[i + 1]
            self.arr[i + 1].left = v
        return self.arr[0]

    def midTraversal(self, root):
        if root is None:
            return
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)
