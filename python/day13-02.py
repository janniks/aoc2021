#!/usr/bin/env python3

# run with:
# cat ../input/day13.txt | ./day13-02.py

import sys
from collections import namedtuple
from functools import partial
from itertools import takewhile
from operator import attrgetter, ne

import numpy as np

Fold = namedtuple('Fold', ['axis', 'value'])

input_dots = list(map(lambda s: list(map(int, s.split(','))), takewhile(partial(ne, ''), map(str.strip, sys.stdin))))
input_folds = list(map(lambda s: Fold(*s.replace('fold along ', '').split('=')), map(str.strip, sys.stdin)))

xs, ys = zip(*input_dots)

paper = np.zeros((max(ys)+1, max(xs)+1), dtype=int)
paper[ys, xs] = 1

def origami(paper, fold):
    matrix = paper.view() if fold.axis == 'y' else np.transpose(paper)

    v = int(fold.value)
    keep = matrix[:v, :].copy()
    cut = np.flipud(matrix[v+1:, :]).copy()

    smaller, larger = sorted([keep, cut], key=attrgetter('shape'))
    diff = larger.shape[0] - smaller.shape[0]
    # pad the smaller with zeroes on top
    smaller = np.pad(smaller, [(diff, 0), (0,0)])

    matrix = larger + smaller

    return matrix if fold.axis == 'y' else np.transpose(matrix)

for fold in input_folds:
    paper = origami(paper, fold)

paper = np.where(paper == 0, ' ', np.where(paper > 0, '#', paper))

np.set_printoptions(edgeitems=100, linewidth=1000)

print('Output:')
print(np.array2string(paper, separator=' ', formatter={'str_kind': lambda x: x}))