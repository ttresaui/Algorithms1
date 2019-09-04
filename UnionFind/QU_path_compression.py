#!/usr/bin/env python
# -*- coding:utf-8 -*-

class QU_Path_Compression(object):
    def __init__(self, N):
        self.id = [i for i in range(int(N))]

    def root(self, p):
        p = int(p)
        while not self.id[p] == p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def connected(self, p, q):
        p, q = int(p), int(q)
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p, q = int(p), int(q)
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

if __name__ == '__main__':
    QF = Quick_Find(10)
    QF.union(5,6)
    print(QF.id)
    QF.union(6, 7)
    print(QF.id)
    QF.union(5, 8)
    print(QF.id)
    QF.union(2, 3)
    print(QF.id)
    QF.union(2, 5)
    print(QF.id)
    print(QF.connected(3,7))