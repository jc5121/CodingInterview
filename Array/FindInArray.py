# -*- coding:utf-8 -*-
# array 二维列表


def Find(target, array):
        if not array:
            return None
        raw_num = len(array)
        col_num = len(array[0])

        i = 0
        j = col_num - 1

        while j >= 0 and i < raw_num:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                i += 1
            elif target < array[i][j]:
                j -= 1

        return False
