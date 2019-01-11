# coding: utf-8
# 操作给定的二叉树，将其变换为源二叉树的镜像。


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    # 返回镜像二叉树根节点, 其实还是原来的root
    def Mirror(self, root):
        if root is None:
            return None
        root_left = root.left
        root.left = root.right
        root.right = root_left
        self.Mirror(root.left)
        self.Mirror(root.right)


