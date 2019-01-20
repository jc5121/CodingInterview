# -*- coding:utf-8 -*-
# 基于交换无法保证原相对顺序不变
# 改变原数组中数的顺序，奇数在前，偶数在后
# 从两边向中间找


def reOrderArray(array):
    i = 0
    j = len(array) - 1
    while i < j:
        if (array[i] % 2 == 1) and (array[j] % 2 == 1):
            i += 1
        elif (array[i] % 2 == 0) and (array[j] % 2 == 1):  # 只有这种情况需要交换
            array[i], array[j] = array[j], array[i]
        elif (array[i] % 2 == 1) and (array[j] % 2 == 0):
            i += 1
            j -= 1
        elif (array[i] % 2 == 0) and (array[j] % 2 == 0):
            j -= 1
    return array


array = [1,2,3,4,5,6,7]

reOrderArray(array)