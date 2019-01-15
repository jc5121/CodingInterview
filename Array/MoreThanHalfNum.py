# -*- coding:utf-8 -*-


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