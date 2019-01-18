# -*- coding:utf-8 -*-
# 动态规划理解
# 例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
# 给一个数组，返回它的最大连续子序列的和


class Solution:

    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return None

        cur_sum = 0  # 记录当前和
        greatest_sum = array[0]  # 不能设置为0，当全是负数时会有问题
        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]  # 之前和若为负，就丢弃
            else:
                cur_sum += array[i]

            if cur_sum > greatest_sum:
                greatest_sum = cur_sum

        return greatest_sum
