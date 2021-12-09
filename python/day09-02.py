#!/usr/bin/env python3

# run with:
# cat ../input/day09.txt | ./day09-01.py

import sys, math
from collections import defaultdict
from functools import partial, reduce
from operator import mul

input = list(map(lambda x: list(map(int, list(x))), map(str.strip, sys.stdin)))

def flat(x): return [z for y in x for z in y]

def mat_enum(lst):
    return [((x, y), h) for x, a in enumerate(lst) for y, h in enumerate(a)]

def sides(c):
    x, y = c
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

def is_low(matrix, item):
    return item[1] < min(map(matrix.__getitem__, sides(item[0])))

def basin_size(matrix, item):
    vstd = set([item[0]])
    prev = [item[0]]
    while prev:
        nxt = set(filter(lambda c: matrix[c] < 9, flat(map(sides, prev)))) - vstd
        vstd |= nxt
        prev = list(nxt)
    return len(vstd)

matrix = defaultdict(lambda: math.inf) | dict(mat_enum(input))

basins = list(map(partial(basin_size, matrix), filter(partial(is_low, matrix), mat_enum(input))))

output = reduce(mul, sorted(basins)[-3:], 1)

print("Output: {output}".format(output=output))
