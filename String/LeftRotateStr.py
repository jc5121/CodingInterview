# -*- coding:utf-8 -*-
# asdfqwer - fqwerasd
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return s
        for i in range(n):
            s += s[i]
        s = s[n:]
        return s