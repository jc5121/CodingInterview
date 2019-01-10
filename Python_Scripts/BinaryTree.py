# -*-: coding: UTF-8 -*-

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None

    # 构造完全二叉树，使用queue
    def add_node(self, data, root):
        node = TreeNode(data)
        if root is None:
            root = node
        else:
            queue = list()
            queue.append(root)
            while True:
                pop_node = queue.pop(0)  # FIFO
                if pop_node.left is None:
                    pop_node.left = node
                    return root
                elif pop_node.right is None:
                    pop_node.right = node
                    return root
                else:
                    queue.append(pop_node.left)
                    queue.append(pop_node.right)
        return root

    # 层次遍历, 借助queue
    def traverse(self, retList, root):
        if root is None:
            return None
        queue = list()
        queue.append(root)
        while len(queue) != 0:
            pop_node = queue.pop(0)
            if pop_node.left is not None:
                queue.append(pop_node.left)
                retList.append(pop_node.left)
            if pop_node.right is not None:
                queue.append(pop_node.right)
                retList.append(pop_node.right)

        return retList

    # 先序
    def preorder(self, retList, root):  # 返回值为参数来解决递归问题，使用时为外部变量
        if root is None:
            return None
        retList.append(root)
        self.preorder(retList, root.left)
        self.preorder(retList, root.right)
        return retList

    # 中序
    def inorder(self, retList, root):
        if root is None:
            return
        self.inorder(retList, root.left)
        retList.append(root)
        self.inorder(retList, root.right)
        return retList

    # 后序
    def postorder(self, retList, root):
        if root is None:
            return
        self.postorder(retList, root.left)
        self.postorder(retList, root.right)
        retList.append(root)
        return retList

    # 重构二叉树，根据先序与中序序列
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None

        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        # 先序像快排 [0] = pivot
        # 中序像归并 [i] = mid
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 6, 8]
    test = Solution()
    newTree = test.reConstructBinaryTree(pre, tin)
    preList = test.preorder([], newTree)
    inList = test.inorder([], newTree)
    postList = test.postorder([], newTree)

    newTree = test.add_node(10, newTree)
    # print (newTree)
    traList = test.traverse([], newTree)

    for i in preList:
        print (i.data)
        
    for i in inList:
        print (i.data)

    for i in postList:
        print (i.data)

    for i in traList:
        print (i.data)
