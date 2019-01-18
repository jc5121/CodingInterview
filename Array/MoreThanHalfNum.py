# -*- coding:utf-8 -*-
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 1.排序之后中位数一定是这个数字，所以可以partition == len/2
# 2.它出现的次数比其他所有数字出现的次数还要多，遍历时当前与前一个相同count++不同count--,
# 这个数字一定是最后一个将count：0->1时对应的。


class Solution:

    def MoreThanHalfNum(self, numbers):

        numbers.sort()  # 先排序，再遍历，很蠢

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