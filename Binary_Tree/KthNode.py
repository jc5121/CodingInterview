# -*- coding:utf-8 -*-
# 中序遍历第k个节点


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot is None or k <= 0:
            return
        root = []  # 没用递归，用的栈结构进行中序遍历
        res = []
        p = pRoot
        while p != None or root != []:
            while p != None:
                root.append(p)
                p = p.left
            if root != []:
                p = root.pop()
                res.append(p)
                p = p.right
        if k > len(res):
            return
        else:
            return res[k-1]