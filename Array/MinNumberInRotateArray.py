# -*- coding:utf-8 -*-
# 旋转数组中的最小数字


def minNumberInRotateArray(rotateArray):
    if not rotateArray:
        return None
    length = len(rotateArray)
    low = 0
    high = length - 1
    mid = low

    while rotateArray[low] >= rotateArray[high]:
        if high - low == 1:  # 找到了
            mid = high
            break

        mid = (low + high) / 2  # 设置mid

        # 三个位置都相等时只能顺序查找了
        if rotateArray[mid] == rotateArray[low] and rotateArray[mid] == rotateArray[high]:
            return FindInOrder(rotateArray, low, high)
        if rotateArray[mid] >= rotateArray[low]:
            low = mid
        if rotateArray[mid] <= rotateArray[high]:
            high = mid
    result = rotateArray[mid]
    return result


def FindInOrder(rotateArray, low, high):
    result = rotateArray[low]
    for i in range(low, high):
        if result < rotateArray[low+i]:
            result = rotateArray[low+i]
    return result