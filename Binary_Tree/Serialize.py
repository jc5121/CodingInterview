# -*- coding:utf-8 -*-
# 序列化和反序列化二叉树
# tree -> list


class TreeNode:

     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:

    def Serialize(self, root):
        if root is not None:
            # 层次遍历，不，应该是先序
            return [root.val] + self.Serialize(root.left) + self.Serialize(root.right)
        else: return ['#']

    def Deserialize(self, s):
        self.s = s
        return self.rDLF()

    def rDLF(self):
        temp = self.s.pop(0)  # 队列，第一个是root
        if temp != '#':
            root = TreeNode(temp)
            root.left = self.rDLF()
            root.right = self.rDLF()
        else: root =None
        return root
