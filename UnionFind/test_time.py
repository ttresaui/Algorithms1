#!/usr/bin/env python
# -*- coding:utf-8 -*-

from QU_path_compression import QU_Path_Compression
from Quick_Find import Quick_Find
from Quick_Union import Quick_Union
from Weighted_QU import Weighted_QU
from Weighted_QU_Path_Compression import Weighted_QU_Path_Compression
import time
import random

class UF_time_test(object):

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.op = self._set_ops()

    def _set_ops(self):
        op = []
        for i in range(self.M):
            a = random.randint(0, self.N -1)
            b = random.randint(0, self.N -1)
            op.append([a, b])
        return op

    def test_QF(self):
        start = time.time()

        QF = Quick_Find(self.N)
        for op in self.op:
            QF.union(op[0], op[1])

        end = time.time()

        print('QF for %s sites, %s ops, Running time: %s Seconds' % (self.N, self.M, (end - start)))

    def test_QU(self):
        start = time.time()

        QF = Quick_Union(self.N)
        for op in self.op:
            QF.union(op[0], op[1])

        end = time.time()

        print('QF for %s sites, %s ops, Running time: %s Seconds' % (self.N, self.M, (end - start)))

    def test_WQU(self):
        start = time.time()

        QF = Weighted_QU(self.N)
        for op in self.op:
            QF.union(op[0], op[1])

        end = time.time()

        print('QF for %s sites, %s ops, Running time: %s Seconds' % (self.N, self.M, (end - start)))

    def test_QUPC(self):
        start = time.time()

        QF = QU_Path_Compression(self.N)
        for op in self.op:
            QF.union(op[0], op[1])

        end = time.time()

        print('QF for %s sites, %s ops, Running time: %s Seconds' % (self.N, self.M, (end - start)))

    def test_WQUPC(self):
        start = time.time()

        QF = Weighted_QU_Path_Compression(self.N)
        for op in self.op:
            QF.union(op[0], op[1])

        end = time.time()

        print('QF for %s sites, %s ops, Running time: %s Seconds' % (self.N, self.M, (end - start)))

if __name__ == '__main__':
    print('-------test for N sites-------')
    for N in [100,1000,10000,100000]:
        UF_test = UF_time_test(N, 1000)
        UF_test.test_WQUPC()

    print('-------test for M ops-------')
    for M in [100, 1000, 10000, 100000]:
        UF_test = UF_time_test(1000, M)
        UF_test.test_WQUPC()
