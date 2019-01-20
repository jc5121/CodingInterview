# -*- coding:utf-8 -*-
# 题目：在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
# 因为字符数目有限，所以可以考虑用两个字典，代表哈希表
# 一个存储每个字符的数量，一个存储只出现一次的字符的位置
# 从位置字典中选取位置最小值作为输出


class Solution:

    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        temp = {}
        temp1 = {}
        for i in range(len(s)):
            if temp.has_key(s[i]):
                temp[s[i]] += 1
            else:
                temp[s[i]] = 1

            if temp[s[i]] == 1:
                temp1[s[i]] = i  # 存位置
            elif temp1.has_key(s[i]):
                del temp1[s[i]]  # 删除
        result = len(s)
        for key in temp1:
            if temp1[key] <= result:
                result = temp1[key]
                continue
        return result