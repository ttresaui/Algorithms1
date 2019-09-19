#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, cargo = None, next = None, prior = None):
        self.cargo = cargo
        self.next = next
        self.prior = prior

class Deque(object):
    def __init__(self):
        self.first = Node()
        self.last = self.first
        self.length = 0

    def isEmpty(self):
        return self.first.cargo == None

    def size(self):
        return self.length

    def addFirst(self, item):
        oldFirst = self.first
        self.length += 1
        if self.isEmpty():
            self.first = Node(item)
            self.last = self.first
        else:
            self.first = Node(item)
            self.first.next = oldFirst
            oldFirst.prior = self.first

    def addLast(self, item):
        oldlast = self.last
        self.length += 1
        if self.isEmpty():
            self.last = Node(item)
            self.first = self.last
        else:
            self.last = Node(item)
            oldlast.next = self.last
            self.last.prior = oldlast

    def removeFirst(self):
        item = self.first.cargo
        if item is None:
            raise Exception('NoSuchElementException')
        else:
            self.length -= 1
            if self.first.next is None:
                self.first.cargo = None
            else:
                self.first = self.first.next
            return item

    def removeLast(self):
        item = self.last.cargo
        if item is None:
            raise Exception('NoSuchElementException')
        else:
            self.length -= 1
            if self.last.prior is None:
                self.last.cargo = None
            else:
                self.last = self.last.prior
            return item

    def iterator(self):
        return self.Iterator(self.first, self.last)

    class Iterator:
        def __init__(self, first, last):
            self.first = first
            self.last = last
            self.current = self.first

        def hasNext(self):
            return self.current != self.last

        def next(self):
            item = self.current.cargo
            self.current = self.current.next
            return item


if __name__ == '__main__':
    deque = Deque()
    deque.addFirst(1)
    deque.addLast(2)
    deque.addFirst(3)
    deque.addLast(4)
    deque.addFirst(5)
    deque.addLast(6)
    deque.addFirst(7)
    deque.addLast(8)
    print(deque.removeLast())
    print(deque.removeFirst())

    i = deque.iterator()
    print(i.next())
    print(i.next())
    print(i.next())

    print(deque.size())