# coding: utf-8
# 数组中最小的n个数，最大堆nlogk
# 1.先将数组中的前k个数取出，构成最大堆，需klogk次比较
# 2.对数组中剩下的n-k个数，每次取出一个，与最大堆的最大值比较。若大，则不操作；
# 若小，则删除此最大值 ，再将该数插入最大堆 ，需logk次比较。总共需(n-k)logk次比较


def GetLeastNumbers_Solution(tinput, k):
    # write code here
    # 这里用list来作为容器，理想是用最大堆，nlogk，这个是nklogk，每插入一次就sort一次不好
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
