# coding: utf-8
# 从上往下打印二叉树


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        res = list()
        level = list()
        if root is None:
            return []
        level.append(root)
        while len(level) != 0:
            pop_node = level.pop(0)
            res.append(pop_node.val)
            if pop_node.left is not None:
                level.append(pop_node.left)
            if pop_node.right is not None:
                level.append(pop_node.right)
        return res
