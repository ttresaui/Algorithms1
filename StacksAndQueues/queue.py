#!/usr/bin/env python
# -*- coding:utf-8 -*-

#使用链表实现队列
class Node(object):
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        #测试
        return str(self.cargo)

class QueueOfString(object):
    def __init__(self):
        self.first = Node()
        self.last = Node()

    def enqueue(self, string):
        oldlast = self.last
        self.last = Node(string)
        if self.isEmpty():
            self.first = self.last
        else:
            oldlast.next = self.last

    def dequeue(self):
        string = self.first.cargo
        self.first = self.first.next
        if self.isEmpty():
            self.last = Node()
        return string

    def isEmpty(self):
        return self.first.cargo == None

    def iterator(self):
        return self.Iterator(self.first)

    class Iterator:
        def __init__(self, first):
            self.current = first

        def hasNext(self):
            return self.current.cargo != None

        def Next(self):
            string = self.current.cargo
            self.current = self.current.next
            return string


#ResizingArray实现栈
class ResizingArrayQueue(object):
    def __init__(self):
        self.s = [None]
        self.head = 0
        self.tail = 0

    def enqueue(self, string):
        if self.tail == len(self.s):
            copy = [None] * ((self.tail - self.head) * 2 + self.head)
            for i in range(self.head, self.tail):
                copy[i] = self.s[i]
            self.s = copy
        self.s[self.tail] = string
        self.tail += 1

    def dequeue(self):
        string = self.s[self.head]
        self.head += 1
        if self.tail - self.head > 0 and self.tail - self.head == int(self.tail / 4):
            copy = [None] * (len(self.s) - int(self.tail / 2))
            for i in range(self.head, self.tail):
                copy[i - int(self.tail/2)] = self.s[i]
                self.head = self.head - int(self.tail / 2)
                self.tail = self.tail - int(self.tail / 2)
            self.s = copy
        return string

    def isEmpty(self):
        return self.head == self.tail

    def iterator(self):
        return self.Iterator(self.s, self.head, self.tail)

    class Iterator:
        def __init__(self, s, head, tail):
            self.s = s
            self.head = head
            self.tail = tail
            self.current = head

        def hasNext(self):
            return self.current < self.tail

        def Next(self):
            string = self.s[self.current]
            self.current += 1
            return string

#python list实现queue
class  PythonListQueue(object):
    def __init__(self):
        self.list = []

    def enqueue(self, string):
        self.list.append(string)

    def dequeue(self):
        string = self.list[0]
        del self.list[0]
        return string

    def isEmpty(self):
        return not self.list

    def iterator(self):
        return self.Iterator(self.list)

    class Iterator:
        def __init__(self, list):
            self.list = list
            self.current = 0

        def hasNext(self):
            return self.current < len(self.list)

        def Next(self):
            string = self.list[self.current]
            self.current += 1
            return string



if __name__ == '__main__':
    Stack = PythonListQueue()
    Stack.enqueue('to')
    Stack.enqueue('be')
    Stack.enqueue('or')
    i = Stack.iterator()
    print(i.Next())
    print(i.Next())
    print(i.Next())
    Stack.enqueue('not')
    Stack.enqueue('to')
    Stack.enqueue('be')
    print(Stack.dequeue())
    print(Stack.dequeue())
    print(Stack.dequeue())
    Stack.enqueue('that')
    Stack.enqueue('is')


