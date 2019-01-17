# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# BST 先中序遍历转化为数组，再转化为双向链表


class Solution:

    # arr = list() 不能写这里
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return None
        self.arr = list()
        self.midTraversal(pRootOfTree)
        for i, v in enumerate(self.arr[:-1]):  # 连接数少2
            v.right = self.arr[i + 1]
            self.arr[i + 1].left = v
        return self.arr[0]

    def midTraversal(self, root):
        if root is None:
            return
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)
