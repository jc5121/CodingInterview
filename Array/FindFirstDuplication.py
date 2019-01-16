# -*- coding:utf-8 -*-
# 找到数组中第一个重复数字，放入duplication[0]中


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False

        copy_buffer = []
        for num in numbers:
            if num in copy_buffer:
                duplication[0] = num
                return True
            copy_buffer.append(num)

        return False
        # write code here