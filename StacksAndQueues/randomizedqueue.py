#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

class RandomizedQueue(object):
    def __init__(self):
        self.s = [None]
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.N):
            copy[i] = self.s[i]
        self.s = copy

    def enqueue(self, item):
        if self.N == len(self.s):
            self.resize(2 * self.N)
        self.s[self.N] = item
        self.N += 1

    def dequeue(self):
        sampleN = random.randint(0, self.N - 1)
        item = self.s[sampleN]
        self.s[sampleN] = self.s[self.N - 1]
        self.N -= 1
        if self.N > 0 and self.N == int(len(self.s) / 4):
            self.resize(int(len(self.s)/2))
        return item

    def sample(self):
        sampleN = random.randint(0, self.N - 1)
        item = self.s[sampleN]
        return item

    def iterator(self):
        return self.Iterator(self.s, self.N)

    class Iterator:
        def __init__(self, s, N):
            self.s = s
            self.N = N
            self.list = list(range(N))
            random.shuffle(self.list)
            self.current = 0

        def hasNext(self):
            return self.current != self.N

        def Next(self):
            item = self.s[self.list[self.current]]
            self.current += 1
            return item

if __name__ == '__main__':
    RQ = RandomizedQueue()
    RQ.enqueue(1)
    RQ.enqueue(2)
    RQ.enqueue(3)
    RQ.enqueue(4)
    RQ.enqueue(5)
    RQ.enqueue(6)
    RQ.enqueue(7)
    RQ.enqueue(8)

    ite = RQ.iterator()
    print(ite.Next())
    print(ite.Next())
    print(ite.Next())
    print(ite.Next())
    print(ite.Next())
    print(ite.Next())
    print(ite.Next())
    print(ite.Next())
  



