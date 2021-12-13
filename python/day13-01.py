#!/usr/bin/env python3

# run with:
# cat ../input/day13.txt | ./day13-01.py

import sys
from functools import partial
from itertools import takewhile
from operator import ne

import numpy as np

input_dots = list(map(lambda s: list(map(int, s.split(','))), takewhile(partial(ne, ''), map(str.strip, sys.stdin))))
input_folds = list(map(lambda s: tuple(s.replace('fold along ', '').split('=')), map(str.strip, sys.stdin)))

xs, ys = zip(*input_dots)
paper = np.zeros((max(ys)+1, max(xs)+1), dtype=int)
paper[ys, xs] = 1

def origami(paper, fold):
    axis, value = fold[0], int(fold[1])
    matrix = paper.view() if axis == 'y' else np.transpose(paper)
    matrix = matrix[:value, :] + np.flipud(matrix[value+1:, :])
    return matrix if axis == 'y' else np.transpose(matrix)

paper = origami(paper, input_folds[0])

output = np.count_nonzero(paper)

print("Output: {output}".format(output=output))
