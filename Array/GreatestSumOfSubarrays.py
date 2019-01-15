# -*- coding:utf-8 -*-

class Solution:

    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return None

        cur_sum = 0
        greatest_sum = array[0]  # 不能设置为0，当全是负数时会有问题
        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]
            else:
                cur_sum += array[i]

            if cur_sum > greatest_sum:
                greatest_sum = cur_sum

        return greatest_sum
