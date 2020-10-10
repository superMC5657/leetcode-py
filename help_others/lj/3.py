# -*- coding: utf-8 -*-
# !@time: 2020/10/9 6:31 下午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 3.py

class NewStack:

    def __init__(self):
        self.stack = []

    def empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise LookupError('stack is empty!')

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise LookupError('stack is empty!')

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):

        if self.a == self.size():
            raise StopIteration
        else:
            self.a += 1
            return self.stack[self.size() - self.a]


stack = NewStack()
stack.stack = [1, 2, 3, 4, 5]
for i in stack:
    print(i)
