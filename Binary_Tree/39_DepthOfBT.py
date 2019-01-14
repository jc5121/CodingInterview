# coding: utf-8
# 二叉树的深度


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        left_depth = self.TreeNode(pRoot.left)
        right_depth = self.TreeNode(pRoot.right)

        return left_depth+1 if left_depth>right_depth else right_depth+1
