# -*- coding:utf-8 -*-
# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
# 要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。


class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        if s.isdigit():
            result = self.StrToIntNumber(s)
        elif s[0] == '+':
            result = self.StrToIntNumber(s[1:])
        elif s[0] == '-':
            result = - + self.StrToIntNumber(s[1:])  # 负数
        else:
            result = 0
        return result

    def StrToIntNumber(self, s):
        result = 0
        j = 0
        for i in range(len(s))[::-1]:
            result += int(s[i]) * pow(10, j)
            j += 1
        return result