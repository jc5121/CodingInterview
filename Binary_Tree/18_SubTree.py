# coding: utf-8
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

from ReConstructBT import TreeNode


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.data == pRoot2.data:  # 跟节点一定相同
                result = self.Tree1HasTree2(pRoot1, pRoot2)
            if result == False:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if result == False:
                result = self.HasSubtree(pRoot1.right, pRoot2)

        return result

    def Tree1HasTree2(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.data != pRoot2.data:
            return False
        return self.Tree1HasTree2(pRoot1.left, pRoot2.left) & \
            self.Tree1HasTree2(pRoot1.right, pRoot2.right)
