# -*- coding: UTF-8 -*-
# 返回[a,b] 其中ab是出现一次的两个数字
# 一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。


class Solution:

    def FindNumsAppearOnce(self, array):
        # write code here
        length = len(array)
        if not array or length < 2:
            return
        resultExclusiveOR = 0  # 全部作异或运算，放入该值
        for i in range(length):
            resultExclusiveOR ^= array[i]
        indexOf1 = 0
        while resultExclusiveOR & 1 != 1:  # 确定与或结果中1的位置
            resultExclusiveOR = resultExclusiveOR >> 1
            indexOf1 += 1
        data1 = 0
        data2 = 0
        for i in range(length):
            if self.IsBit1(array[i], indexOf1):  # 确定分组，第indexOf1位是不是1
                data1 ^= array[i]
            else:
                data2 ^= array[i]
        result = [data1, data2]
        return result

    def IsBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1