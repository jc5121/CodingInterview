# -*- coding:utf-8 -*-
# 两个栈，一个负责保存数据，一个跟踪记录最小值，底层数据结构都用list


class Solution:
    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, node):
        if len(self.stack) == 0:
            self.min_val.append(node)
        elif self.min_val[-1] >= node:
            self.min_val.append(node)

        self.stack.append(node)

    def pop(self):
        if self.stack[-1] == self.min_val[-1]:
            self.min_val.pop()
        self.stack.pop()

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]

    def min(self):
        if len(self.min_val) != 0:
            return self.min_val[-1]