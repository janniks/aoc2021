#!/usr/bin/env python3

# run with:
# cat ../input/day09.txt | ./day09-01.py

import sys, math
from collections import defaultdict
from functools import partial

input = list(map(lambda x: list(map(int, list(x))), map(str.strip, sys.stdin)))

def menum(lst):
    return [((x, y), h) for x, a in enumerate(lst) for y, h in enumerate(a)]

def sides(c):
    x, y = c
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

def is_low(matrix, item):
    return item[1] < min(map(matrix.__getitem__, sides(item[0])))

matrix = defaultdict(lambda: math.inf) | dict(menum(input))

output = sum(map(lambda x: x[1]+1, filter(partial(is_low, matrix), menum(input))))

print("Output: {output}".format(output=output))
