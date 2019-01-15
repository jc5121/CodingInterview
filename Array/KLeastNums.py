# coding: utf-8
# 数组中最小的n个数


def GetLeastNumbers_Solution(tinput, k):
    # write code here
    # 这里用链表来作为容器，理想是用最大堆，nlogk，这个是nklogk，每插入一次就sort一次不好
    result = []
    if tinput == [] or k <= 0 or k > len(tinput):
        return result
    for i in range(len(tinput)):
        if len(result) < k:
            result.append(tinput[i])
            result.sort()
        elif tinput[i] >= result[len(result) - 1] and len(result) == k:
            continue
        elif tinput[i] < result[len(result) - 1]:
            result.pop()
            result.append(tinput[i])
            result.sort()
    return result
