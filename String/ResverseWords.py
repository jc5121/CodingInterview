# -*- coding:utf-8 -*-
# student. a am I - I am a student.


class Solution:
    def ReverseSentence(self, s):
        # write code here
        s = s.split(' ')
        result = []
        for ch in s[::-1]:  # [::-1]反转s中所有ch顺序， 一步到位
            result.append(ch)
        result = ' '.join(result)
        return result