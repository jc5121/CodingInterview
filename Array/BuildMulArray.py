# -*- coding:utf-8 -*-
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 不能使用除法。


class Solution:
    def mul(self, a, b):
        return a * b

    def multiply(self, A):

        if not A:
            return
        A1, B = [], []
        length = len(A)
        for i in range(length):
            A1 = A[:i] + A[i + 1:]
            B.append(reduce(self.mul, A1))
        return B
