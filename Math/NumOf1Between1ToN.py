# -*- coding:utf-8 -*-
# 从1到n整数中1出现的次数


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 0:
            return 0
        # n = str(n)
        return self.NumberOf1(n)

    def NumberOf1(self, n):
        n = str(n)
        first = int(n[0])
        length = len(n)
        if length == 1 and first == 0:
            return 0
        if length == 1 and first > 0:
            return 1

        # 第一部分最高位中1出现的次数
        numFirstDigit = 0
        if first > 1:
            numFirstDigit = self.PowerBase10(length - 1)
        elif first == 1:
            numFirstDigit = int(n[1:]) + 1

        # 第一部分其他位中1出现的次数
        numOtherDigits = first * (length - 1) * self.PowerBase10(length - 2)

        # 第二部分
        numRescursive = self.NumberOf1(n[1:])

        return numFirstDigit + numOtherDigits + numRescursive

    def PowerBase10(self, n):
        result = 1
        for i in range(n):
            result *= 10
        return result