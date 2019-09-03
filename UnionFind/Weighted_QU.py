#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Quick_Find(object):
    def __init__(self, N):
        self.id = [i for i in range(int(N))]
        self.size = [1 for i in range(int(N))]

    def root(self, p):
        p = int(p)
        while not self.id[p] == p:
            p = self.id[p]
        return p

    def connected(self, p, q):
        p, q = int(p), int(q)
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p, q = int(p), int(q)
        i = self.root(p)
        j = self.root(q)
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]

if __name__ == '__main__':
    QF = Quick_Find(10)
    QF.union(5,6)
    print(QF.id, QF.size)
    QF.union(6, 7)
    print(QF.id, QF.size)
    QF.union(8, 7)
    print(QF.id, QF.size)
    QF.union(2, 3)
    print(QF.id, QF.size)
    QF.union(2, 6)
    print(QF.id, QF.size)
    print(QF.connected(3,7))