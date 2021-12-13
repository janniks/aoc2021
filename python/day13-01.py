#!/usr/bin/env python3

# run with:
# cat ../input/day13.txt | ./day13-01.py

import sys
from collections import namedtuple
from functools import partial
from itertools import takewhile
from operator import ne

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
    matrix = matrix[:v, :] + np.flipud(matrix[v+1:, :])
    return matrix if fold.axis == 'y' else np.transpose(matrix)

paper = origami(paper, input_folds[0])

output = np.count_nonzero(paper)

print("Output: {output}".format(output=output))
