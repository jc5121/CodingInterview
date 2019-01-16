# -*- coding:utf-8 -*-
# 判断字符串是否能表示数字，主要考虑代码的全面性
class Solution:
    # s字符串

    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        s = self.scannumber(s)
        while s:
            if s[0] == '.':
                s = self.scannumber(s[1:])
            while s:
                if s[0] == 'e' or s[0] == 'E':
                    if not s[1:]:
                        return False
                    if s[1] == '+' or s[1] == '-':
                        if not s[2:]:
                            return False
                        s = s[2:]
                    else:
                        s = s[1:]
                    s = self.scannumber(s)
                    if s:
                        return False
                else:
                    return False
        return True

    def scannumber(self, s):
        while s:
            if s[0].isdigit():
                s = s[1:]
            else:
                break
        return s
