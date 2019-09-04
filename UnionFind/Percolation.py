#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Weighted_QU_Path_Compression import Weighted_QU_Path_Compression

class Percolation(object):

    def __init__(self, N):
        self.N = int(N)
        self.WQUPC = Weighted_QU_Path_Compression(self.N**2 + 2)
        self.isopen = [False for i in range(self.N**2 + 2)]
        self.isopen[-2:] = [True, True]

    def index(self, row, col):
        row, col = int(row), int(col)
        return int(self.N * (row - 1) + col - 1)

    def nearbysites(self, row, col):
        row, col = int(row), int(col)
        sitesindex = []
        if col > 1:
            leftsite = index(row, col) - 1
            sitesindex.append(leftsite)
        elif col < self.N:
            rightsite = index(row, col) + 1
            sitesindex.append(rightsite)
        elif row > 1:
            upsite = index(row, col) - self.N
            sitesindex.append(upsite)
        elif row < self.N:
            downsite = index(row, col) + self.N
            sitesindex.append(downsite)
        return sitesindex

    def open(self, row, col):
        index = self.index(row, col)
        self.isopen[index] = True
        if row == 1:
            self.WQUPC.Union(index, self.N**2)
        elif row == self.N:
            self.WQUPC.Union(index, self.N**2 + 1)
        for nearindex in self.nearbysites(row, col):
            if self.isOpen(nearindex):
                self.WQUPC.Union(index, nearindex)

    def isOpen(self, row, col):
        return self.isopen[self.index(row, col)]

    def isFull(self, row, col):
        return self.WQUPC.connected(self.index(row, col), self.N**2)

    def numberOfOpenSites(self):
        return sum(self.isopen) - 2

    def percolates(self):
        return self.WQUPC.connected(self.N**2, self.N**2+1)


if __name__ == '__main__':
    Percolation = Percolation(10)
    print(Percolation.WQUPC.id)
    print(Percolation.isopen)


