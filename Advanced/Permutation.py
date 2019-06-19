# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        res = []
        self.backtrace(sorted(ss),'',res)
        return res
        # write code here
    def backtrace(self, ss, path, res):
        if len(ss) == 0 and path not in res:
            res.append(path)
            return
        for i in range(len(ss)):
            self.backtrace(ss[:i]+ss[i+1:], path+ss[i], res)
