#!/usr/bin/env python
# -*- coding:utf-8 -*-

#使用链表实现栈
class Node(object):
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        #测试
        return str(self.cargo)

class StackOfString(object):
    def __init__(self):
        self.first = Node()

    def push(self, string):
        oldfirst = self.first
        self.first = Node(string, oldfirst)

    def pop(self):
        string = self.first.cargo
        self.first = self.first.next
        return string

    def isEmpty(self):
        return self.first.cargo == None

    def iterator(self):

        return self.Iterator(self.first)

    class Iterator:
        def __init__(self, first):
             self.current = first

        def hasNext(self):
            return self.current.next.cargo != None

        def Next(self):
            string = self.current.cargo
            self.current = self.current.next
            return string



#ResizingArray实现栈
class ResizingArrayStack(object):
    def __init__(self):
        self.s = [None]
        self.N = 0

    def push(self, string):
        if self.N == len(self.s):
            self.resize(2 * len(self.s))
        self.s[self.N] = string
        self.N += 1

    def resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.N):
            copy[i] = self.s[i]
        self.s = copy

    def pop(self):
        string = self.s[self.N -1]
        self.N -= 1
        if self.N > 0 and self.N == int(len(self.s) / 4):
            self.resize(int(len(self.s)/2))
        return string

    def isEmpty(self):
        return self.N == 0

    def iterator(self):
        return self.Iterator(self.s, self.N)

    class Iterator:
        def __init__(self, s, N):
            self.currentS = s
            self.current = N

        def hasNext(self):
            return self.current > 0

        def Next(self):
            string = self.currentS[self.current - 1]
            self.current -= 1
            return string


#封装python的list结果实现栈
class PythonListStack(object):
    def __init__(self):
        self.list = []

    def push(self, string):
        self.list.append(string)

    def pop(self):
        string = self.list.pop()
        return string

    def isEmpty(self):
        return not self.list

    def iterator(self):
        return self.Iterator(self.list)

    class Iterator:
        def __init__(self, list):
            self.current = list
            self.i = len(list)

        def hasNext(self):
            return self.current > 0

        def Next(self):
            string = self.current[self.i - 1]
            self.i -= 1
            return string


if __name__ == '__main__':
    Stack = PythonListStack()
    Stack.push('to')
    Stack.push('be')
    Stack.push('or')
    Stack.push('not')
    Stack.push('to')
    i = Stack.iterator()
    print(i.Next())
    print(i.Next())
    print(i.Next())
    print(Stack.pop())
    Stack.push('be')
    print(Stack.pop())
    print(Stack.pop())
    Stack.push('that')
    print(Stack.pop())
    print(Stack.pop())
    print(Stack.pop())
    Stack.push('is')


