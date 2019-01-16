# -*- coding:utf-8 -*-
# 按照 之 字打印二叉树

import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        q = Queue.Queue()
        result = []
        q.put(pRoot)
        j = 1
        while not q.empty():  # 层次遍历
            level = []
            length = q.qsize()
            for i in range(length):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if j%2 == 0:
                print level
                level = level[::-1]  # 反转
                print level
            result.append(level)
            j += 1
        return result