# -*- coding:utf-8 -*-


class Solution:

    def IsPopOrder(self, pushV, popV):

        tempstack = []  # 使用一个栈进行模拟
        for ch in pushV:  # 边压入边弹出
            tempstack.append(ch)
            # 每进行一次压入就判断一次
            while tempstack != []:
                if tempstack[-1] == popV[0]:
                    popV = popV[1:]
                    tempstack.pop()
                else:
                    break
        if tempstack ==[] and popV ==[]:
            result = True
        else:
            result = False
        return result

