# -*- coding: UTF-8 -*-
# 归并排序，不需要交换。
import numpy as np


def merge(lyst, copyBuffer, low, middle, high):
    i = low
    j = middle + 1

    for k in range(low, high + 1):
        if i > middle:
            copyBuffer[k] = lyst[j]
            j += 1
        elif j > high:  # 必须是elif
            copyBuffer[k] = lyst[i]
            i += 1
        elif lyst[i] < lyst[j]:
            copyBuffer[k] = lyst[i]
            i += 1
        else:
            copyBuffer[k] = lyst[j]
            j += 1

    for k in range(low, high + 1):
        lyst[k] = copyBuffer[k]


def mergeSortHelper(lyst, copyBuffer, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, mid)
        mergeSortHelper(lyst, copyBuffer, mid + 1, high)
        merge(lyst, copyBuffer, low, mid, high)


def mergeSort(lyst):
    copyBuffer = range(len(lyst))  # 用这种方法初始化
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)


if __name__ == "__main__":
    lyst = np.random.randint(10, size=10)  # 该函数返回类型是martix不是list
    print lyst
    mergeSort(lyst)
    print lyst
