# -*- coding: UTF-8 -*-
# 快速排序。
import numpy as np


def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]


def partition(lyst, low, high):
    i = low
    j = high
    pivot = lyst[low]

    while True:
        # 2个while都要 = 否则出现 [a, a, ..., a]会无限循环
        while lyst[i] <= pivot:
            i += 1
            if i == high: break

        while lyst[j] >= pivot:
            j -= 1
            if j == low: break

        if i >= j: break

        swap(lyst, i, j)

    swap(lyst, low, j)

    return j


def quickSortHelper(lyst, low, high):
    if low >= high:
        return
    pivotLocation = partition(lyst, low, high)
    quickSortHelper(lyst, low, pivotLocation - 1)
    quickSortHelper(lyst, pivotLocation + 1, high)


def quickSort(lyst):
    quickSortHelper(lyst, 0, len(lyst) - 1)


if __name__ == "__main__":
    lyst = np.random.randint(10, size=10)
    print lyst
    quickSort(lyst)
    print lyst
