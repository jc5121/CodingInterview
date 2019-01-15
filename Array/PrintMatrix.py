# -*- coding: UTF-8 -*-
# 顺时针打印二维矩阵
# 熟练使用pop，所有打印过的都pop
# matrix.pop返回横行
# row.pop()返回一个


def printMatrix(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)  # 1.打印第一行
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())  # 2.打印最右一列
        if matrix:
            res += matrix.pop()[::-1]  # 3.打印最下面一行
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))  # 4.打印最左一列
    return res