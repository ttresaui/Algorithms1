#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Percolation import Percolation
from random import choice
import numpy as np

class PercolationStats(object):

    def __init__(self, N, trials):
        self.N = int(N)
        self.trials = int(trials)
        self.X = []
        self.Ttrials()

    def one_trial(self):
        Per = Percolation(self.N)
        while not Per.percolates():
            open_index = choice([index for index, value in enumerate(Per.isopen) if not value])
            row, col = Per.row_col(open_index)
            Per.open(row, col)
        return Per.numberOfOpenSites()

    def Ttrials(self):
        for num in range(self.trials):
            self.X.append(self.one_trial())

    def mean(self):
        return np.mean(self.X)

    def stddev(self):
        return np.std(self.X, ddof=1)

    def confidenceLo(self):
        return (self.mean() - 1.96 * self.stddev() / np.sqrt(self.trials))

    def confidenceHi(self):
        return (self.mean() + 1.96 * self.stddev() / np.sqrt(self.trials))

if __name__ == '__main__':
    PercolationStats = PercolationStats(100, 10)
    print('mean: %s' % PercolationStats.mean())
