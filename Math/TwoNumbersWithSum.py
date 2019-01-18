# coding: utf-8
# 输入一个递增排序的数组和一个数字S，
# 在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# 两边向中间找


def FindNumbersWithSum(array, tsum):
    # write code here
    i = 0
    j = len(array) - 1
    result = []
    while i < j:
        sum = int(array[i]) + int(array[j])
        if sum == tsum:
            multi = int(array[i]) * int(array[j])
            if result == []:
                tempmulti = multi
                result.append(int(array[i]))
                result.append(int(array[j]))
            elif multi < tempmulti:
                tempmulti = multi
                result.append(int(array[i]))
                result.append(int(array[j]))
            i += 1
            j -= 1
        elif sum < tsum:
            i += 1
        else:
            j -= 1
    return result