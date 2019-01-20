# coding: utf-8
# 题目：排序数组中k出现的次数
# 二分法查找最前面的数的位置和最后面的数的位置


class Solution:

    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        length = len(data)
        first = self.GetFirstK(data, k, 0, length-1)
        last = self.GetLastK(data, k, 0, length-1)
        if first != -1 and last != -1:
            return last-first+1
        else:
            return 0

    def GetFirstK(self, data, k, start, end):
        if start > end:
            return -1
        length = len(data)
        midIndex = (start + end) / 2
        mideData = data[midIndex]
        if mideData == k:
            if (midIndex < length - 1 and data[midIndex-1] != k) or midIndex == 0:
                return midIndex
            else:
                end = midIndex - 1  # 这里决定了是找开头的k
        elif mideData < k:
            start = midIndex + 1
        else:
            end = midIndex - 1
        return self.GetFirstK(data, k, start, end)

    def GetLastK(self, data, k, start, end):
        if start > end:
            return -1
        length = len(data)
        midIndex = (start + end) / 2
        midData = data[midIndex]
        if midData == k:
            if (midIndex < length - 1 and data[midIndex+1] != k) or midIndex == length-1:
                return midIndex
            else:
                start = midIndex + 1  # 这里决定了是找末尾的k
        elif midData < k:
            start = midIndex + 1
        else:
            end = midIndex - 1
        return self.GetLastK(data, k, start, end)