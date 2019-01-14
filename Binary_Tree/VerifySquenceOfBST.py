# coding: utf-8
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。


def VerifySquenceOfBST(squence):
    if squence is None:
        return False

    root = squence[-1]
    length = len(squence)

    for i in range(length):
        if squence[i] > root:  # 找到右子树最小节点
            break

    for j in range(i, length):
        if squence[j] < root:
            return False

    left = True
    right = True

    if i > 0:
        left = VerifySquenceOfBST(squence[0:i])
    if i < length - 1:
        right = VerifySquenceOfBST(squence[i:length-1])

    return left and right


a = []  # not None why ?
if a is not None:
    print 'd'