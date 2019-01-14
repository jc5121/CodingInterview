# coding: utf-8
# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。


class Solution:

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        route = []
        currentsum = 0  # 注意这三个参数的传递方式，有点像作为全局变量来用的。
        if root is None:
            return result
        result = self.Path(root, expectNumber, route, currentsum, result)
        return result

    def Path(self, root, expectNumber, route, currentsum, result):
        currentsum += root.val
        route.append(root)
        # 如果是叶子结点，存入result
        isleaf = (root.left == None and root.right == None)
        if currentsum == expectNumber and isleaf:
            onepath = []
            for node in route:
                onepath.append(node.val)
            result.append(onepath)
        # 如果不是叶子结点，则遍历它的子结点
        if root.left != None:
            self.Path(root.left, expectNumber, route, currentsum, result)
        if root.right != None:
            self.Path(root.right, expectNumber, route, currentsum, result)
        # 在返回到父结点之前，在路径上删除当前结点，并在currentsum中减去当前结点的值
        # 无论是否成功都要返回的，很像深度优先遍历
        currentsum -= root.val
        route.pop()
        return result
