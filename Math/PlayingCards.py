# -*- coding:utf-8 -*-
# 随机抽5张是不是顺子，王是赖子，看作0
# 先排序 !!!


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        length = len(numbers)
        if not numbers or length < 1:
            return False
        numbers.sort()  # 先排序
        NumberOfZero = 0
        NumberOfGap = 0
        for i in range(length-1):  # -1了，保证数组不越界
            if numbers[i] == 0:
                NumberOfZero += 1
                continue
            if numbers[i] == numbers[i+1]:  # 有对子不可能是顺子
                return False
            NumberOfGap += numbers[i+1] - numbers[i] - 1  # 要多剪1才算空隙
        if NumberOfZero >= NumberOfGap:  # 0 树目大于等于空隙数，则是顺子
            return True
        else:
            return False