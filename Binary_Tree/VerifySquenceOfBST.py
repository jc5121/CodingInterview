# coding: utf-8
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。


def VerifySequenceOfBST(sequence):
    if sequence is None:
        return False

    root = sequence[-1]
    length = len(sequence)

    for i in range(length):
        if sequence[i] > root:  # 找到右子树最小节点
            break

    for j in range(i, length):
        if sequence[j] < root:
            return False

    left = True
    right = True

    if i > 0:
        left = VerifySequenceOfBST(sequence[0:i])
    if i < length - 1:
        right = VerifySequenceOfBST(sequence[i:length-1])

    return left and right


a = []  # not None why ?
if a is not None:
    print 'd'