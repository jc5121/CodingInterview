# -*- coding:utf-8 -*-
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。


class Solution:

    def MoreThanHalfNum(self, numbers):

        numbers.sort()  # 先排序

        current = numbers[0]
        times = 1

        for i in range(0, len(numbers)):
            if numbers[i] == current:
                times += 1
                if times > len(numbers)/2:
                    return numbers[i]
            else:
                current = numbers[i]
                times = 1
        return 0