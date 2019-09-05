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

    def row_col(self, index):
        row = int(index)//int(self.N) + 1
        col = int(index)%int(self.N) + 1
        return row, col

    def nearbysites(self, row, col):
        row, col = int(row), int(col)
        sitesindex = []
        if col > 1:
            leftsite = self.index(row, col) - 1
            sitesindex.append(leftsite)
        elif col < self.N:
            rightsite = self.index(row, col) + 1
            sitesindex.append(rightsite)

        if row > 1:
            upsite = self.index(row, col) - self.N
            sitesindex.append(upsite)
        elif row < self.N:
            downsite = self.index(row, col) + self.N
            sitesindex.append(downsite)
        return sitesindex

    def open(self, row, col):
        index = self.index(row, col)
        if not self.isopen[index]:
            self.isopen[index] = True
            if row == 1:
                self.WQUPC.union(index, self.N**2)
            elif row == self.N:
                self.WQUPC.union(index, self.N**2 + 1)
            for nearindex in self.nearbysites(row, col):
                if self.isOpen(nearindex):
                    self.WQUPC.union(index, nearindex)

    def isOpen(self, index):
        return self.isopen[index]

    def isFull(self, row, col):
        return self.WQUPC.connected(self.index(row, col), self.N**2)

    def numberOfOpenSites(self):
        return sum(self.isopen) - 2

    def percolates(self):
        return self.WQUPC.connected(self.N**2, self.N**2+1)


if __name__ == '__main__':
    Percolation = Percolation(10)
    Percolation.open(1,5)
    Percolation.open(2, 5)
    Percolation.open(3, 5)
    Percolation.open(4, 5)
    Percolation.open(5, 5)
    Percolation.open(6, 5)
    Percolation.open(7, 5)
    Percolation.open(8, 5)
    Percolation.open(9, 5)
    Percolation.open(9, 6)
    Percolation.open(10, 6)
    print(Percolation.isFull(9, 5))
    print(Percolation.percolates())
    print(Percolation.numberOfOpenSites())
    print(Percolation.index(3,8))
    print(Percolation.row_col(27))



