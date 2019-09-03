#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Quick_Find(object):
    def __init__(self, N):
        self.id = [i for i in range(int(N))]

    def connected(self, p, q):
        p, q = int(p), int(q)
        return self.id[p] == self.id[q]

    def union(self, p, q):
        p, q = int(p), int(q)
        pid = self.id[p]
        qid = self.id[q]
        for index, value in enumerate(self.id):
            if value == pid:
                self.id[index] = qid

if __name__ == '__main__':
    QF = Quick_Find(10)
    QF.union(5,6)
    print(QF.id)
    QF.union(6, 7)
    print(QF.id)
    QF.union(8, 7)
    print(QF.id)
    QF.union(2, 3)
    print(QF.id)
    QF.union(2, 6)
    print(QF.id)
    print(QF.connected(3,7))