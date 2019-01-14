# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def depth(self, pRoot):
        if pRoot is None:
            return 0
        left_depth = self.depth(pRoot.left)
        right_depth = self.depth(pRoot.right)
        return left_depth + 1 if left_depth > right_depth else right_depth + 1


    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        if self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right):
            diff = self.depth(pRoot.left) - self.depth(pRoot.right)
            if abs(diff) <= 1:
                return True
            else:
                return False

